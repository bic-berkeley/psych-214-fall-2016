""" Run non-linear registration using dipy
"""

import sys
import os
from os.path import split as psplit, join as pjoin, splitext, exists
import pickle

string_type = str if sys.version_info[0] > 2 else basestring

import numpy as np
import numpy.linalg as npl

import nibabel as nib
from nibabel.affines import to_matvec

from scipy.ndimage import affine_transform

from dipy.align.imaffine import (MutualInformationMetric, AffineRegistration)
from dipy.align.transforms import (TranslationTransform3D,
                                   RigidTransform3D,
                                   AffineTransform3D)
from dipy.align.imwarp import SymmetricDiffeomorphicRegistration
from dipy.align.metrics import CCMetric


TEMPLATE_IMG = 'mni_icbm152_t1_tal_nlin_asym_09a.nii'
TEMPLATE_MASK = 'mni_icbm152_t1_tal_nlin_asym_09a_mask.nii'


def as_image(image):
    """ If `image` is string, assume filename and load image, else pass through
    """
    if isinstance(image, string_type):
        image = nib.load(image)
    return image


def apply_mask(brain_img, mask_img):
    """ Load brain image, matching mask; apply and return masked image

    Parameters
    ----------
    brain_img : str or image
        string giving image filename or image object
    mask_img : str or image
        string giving mask image filename or image object.  Mask must match
        `brain_img` after mapping with image and mask affine.

    Returns
    -------
    mask_img : image object
        image object where data is data from `brain_img` multiplied elementwise
        by the data of `mask_img`, where the mask data has[ been resampled into
        the voxel space of `brain_img` if necessary.
    """
    brain_img = as_image(brain_img)
    b_aff = brain_img.affine
    b_hdr = brain_img.header
    mask_img = as_image(mask_img)
    brain_data = brain_img.get_data()
    mask_data = mask_img.get_data()
    if not np.allclose(b_aff, mask_img.affine):
        # Mask and brain have different affines - we need to resample
        brain2mask = npl.inv(mask_img.affine).dot(brain_img.affine)
        mat, vec = to_matvec(brain2mask)
        mask_data = affine_transform(mask_data, mat, vec,
                                     output_shape=brain_data.shape,
                                     order=0)  # nearest neighbor
    return nib.Nifti1Image(brain_data * mask_data, b_aff, b_hdr)


def register_affine(t_masked, m_masked, affreg=None,
                    final_iters=(10000, 1000, 100)):
    """ Run affine registration between images `t_masked`, `m_masked`

    Parameters
    ----------
    t_masked : image
        Template image object, with image data masked to set out-of-brain
        voxels to zero.
    m_masked : image
        Moving (individual) image object, with image data masked to set
        out-of-brain voxels to zero.
    affreg : None or AffineRegistration instance, optional
        AffineRegistration with which to register `m_masked` to `t_masked`.  If
        None, we make an instance with default parameters.
    final_iters : tuple, optional
        Length 3 tuple of level iterations to use on final affine pass of the
        registration.

    Returns
    -------
    affine : shape (4, 4) ndarray
        Final affine mapping from voxels in `t_masked` to voxels in `m_masked`.
    """
    if affreg is None:
        metric = MutualInformationMetric(nbins=32,
                                         sampling_proportion=None)
        affreg = AffineRegistration(metric=metric)
    t_data = t_masked.get_data().astype(float)
    m_data = m_masked.get_data().astype(float)
    t_aff = t_masked.affine
    m_aff = m_masked.affine
    translation = affreg.optimize(t_data, m_data, TranslationTransform3D(),
                                  None, t_aff, m_aff)
    rigid = affreg.optimize(t_data, m_data, RigidTransform3D(), None, t_aff,
                            m_aff, starting_affine=translation.affine)
    # Maybe bump up iterations for last step
    if final_iters is not None:
        affreg.level_iters = list(final_iters)
    affine = affreg.optimize(t_data, m_data, AffineTransform3D(), None, t_aff,
                             m_aff, starting_affine=rigid.affine)
    return affine.affine


def register_diffeo(t_masked, m_masked, start_affine, registration=None):
    """ Run non-linear registration between `t_masked` and `m_masked`

    Parameters
    ----------
    t_masked : image
        Template image object, with image data masked to set out-of-brain
        voxels to zero.
    m_masked : image
        Moving (individual) image object, with image data masked to set
        out-of-brain voxels to zero.
    start_affine : shape (4, 4) ndarray
        Affine mapping from voxels in `t_masked` to voxels in `m_masked`.
    registration : None or SymmetricDiffeoMorphicRegistration instance
        Registration instance we will use to register `t_masked` and
        `m_masked`.  If None, make a default registration object.

    Returns
    -------
    mapping : mapping instance
        Instance giving affine + non-linear mapping between voxels in
        `t_masked` and voxels in `m_masked`.
    """
    if registration is None:
        registration = SymmetricDiffeomorphicRegistration(
            metric=CCMetric(3),
            level_iters=[10, 10, 5])
    return registration.optimize(t_masked.get_data().astype(float),
                                 m_masked.get_data().astype(float),
                                 t_masked.affine,
                                 m_masked.affine,
                                 start_affine)


def register_save(template_fname, template_mask_fname,
                  moving_fname, moving_mask_fname):
    path, basename = psplit(moving_fname)
    root, ext = splitext(basename)
    if ext == '.gz':  # ignore .gz suffix
        root, ext = splitext(root)
    t_masked = apply_mask(template_fname, template_mask_fname)
    m_masked = apply_mask(moving_fname, moving_mask_fname)
    affine = register_affine(t_masked, m_masked)
    mapping = register_diffeo(t_masked, m_masked, affine)
    masked_data = m_masked.get_data()
    warped_moving = nib.Nifti1Image(mapping.transform(masked_data),
                                    t_masked.affine,
                                    t_masked.header)
    nib.save(warped_moving, pjoin(path, 'w_' + basename))
    with open(pjoin(path, 'map_' + root + '.pkl'), 'wb') as fobj:
        pickle.dump(mapping, fobj)
    return mapping


def as_mapping(mapping):
    """ If `mapping` is string, assume filename, load pickle, else pass through
    """
    if isinstance(mapping, string_type):
        with open(mapping, 'rb') as fobj:
            mapping = pickle.load(fobj)
    return mapping


def write_warped(fname, mapping, interpolation='nearest', template_header=None):
    """ Warp an image in individual space to template space

    Parameters
    ----------
    fmame : str
        Filename of image to warp in template space
    """
    img = nib.load(fname)
    mapping = as_mapping(mapping)
    template_affine = mapping.codomain_grid2world
    data = img.get_data().astype(float)
    warped = mapping.transform(data, interpolation=interpolation)
    warped_img = nib.Nifti1Image(warped, template_affine, template_header)
    path, basename = psplit(fname)
    out_fname = pjoin(path, 'w_' + basename)
    nib.save(warped_img, out_fname)


def find_anatomicals(path):
    anatomicals = []
    for dirpath, dirnames, filenames in os.walk(path):
        if not 'highres001.nii.gz' in filenames:
            continue
        full_image = pjoin(dirpath, 'highres001.nii.gz')
        mask_image = pjoin(dirpath, 'highres001_brain_mask.nii.gz')
        assert exists(full_image)
        assert exists(mask_image)
        anatomicals.append((mask_image, full_image))
    return anatomicals


def sub2img_mask(root, sub_no):
    anatomical_path = pjoin(root, 'sub{:03d}'.format(sub_no), 'anatomy')
    ret = (pjoin(anatomical_path, 'highres001.nii.gz'),
           pjoin(anatomical_path, 'highres001_brain_mask.nii.gz'))
    if all(exists(p) for p in ret):
        return ret
    return ()


def write_highres(path):
    for moving_img, moving_mask in find_anatomicals(path):
        register_save(TEMPLATE_IMG, TEMPLATE_MASK,
                      moving_img, moving_mask)


def write_highres_parallel(path):
    import multiprocessing
    jobs = []
    for moving_img, moving_mask in find_anatomicals(path):
        p = multiprocessing.Process(target=register_save, args=(
            TEMPLATE_IMG, TEMPLATE_MASK, moving_img, moving_mask))
        jobs.append(p)
        p.start()


def register_subject(root, sub_no):
    moving_img, moving_mask = sub2img_mask(root, sub_no)
    return register_save(TEMPLATE_IMG, TEMPLATE_MASK,
                         moving_img, moving_mask)
