""" Affine optimization exercise
"""

#: standard imports
import numpy as np
import matplotlib.pyplot as plt
# print arrays to 4 decimal places
np.set_printoptions(precision=4, suppress=True)
import numpy.linalg as npl
import nibabel as nib

#: gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

#: Check import of rotations code
from rotations import x_rotmat, y_rotmat, z_rotmat

#: ds114 subject 9 highres, skull stripped
subject_img = nib.load('ds114_sub009_highres_brain_222.nii')
subject_data = subject_img.get_data()
subject_data.shape

#: an example slice of skull-stripped structural
plt.imshow(subject_data[:, :, 80])

#: the MNI template - also skull stripped
template_img = nib.load('mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii')
template_data = template_img.get_data()
template_data.shape

#: example slice over the third dimension of the template
plt.imshow(template_data[:, :, 42])

#- Get affine mapping from template voxels to subject voxels

#- Break up `template_vox2subject_vox` into 3x3 `mat` and
#- length 3 `vec`

#- Use affine_transform to make a copy of the subject image
#- resampled into the array dimensions of the template image
#- Call this resampled copy `subject_resampled`
#- (we are going to use this array later).
#- Use order=1 for the resampling (it is quicker)

#- Plot slice from resampled subject data next to slice
#- from template data

#: the negative correlation mismatch metric
def correl_mismatch(x, y):
    """ Negative correlation between the two images, flattened to 1D
    """
    x_mean0 = x.ravel() - x.mean()
    y_mean0 = y.ravel() - y.mean()
    corr_top = x_mean0.dot(y_mean0)
    corr_bottom = (np.sqrt(x_mean0.dot(x_mean0)) *
                   np.sqrt(y_mean0.dot(y_mean0)))
    return -corr_top / corr_bottom

#: check numpy agrees with our negative correlation calculation
x = np.random.normal(size=(100,))
y = np.random.normal(size=(100,))
assert np.allclose(correl_mismatch(x, y), -np.corrcoef(x, y)[0, 1])

#- Make params2affine function
#- * accepts params vector
#- * builds matrix for zooms
#- * builds atrix for rotations
#- * builds vector for translations
#- * compile into affine and return

#: some checks that the function does the right thing
# Identity params gives identity affine
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0, 1, 1, 1]),
                   np.eye(4))
# Some zooms
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0, 2, 3, 4]),
                   np.diag([2, 3, 4, 1]))
# Some translations
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0, 2, 3, 4]),
                   np.diag([2, 3, 4, 1]))
# Some rotations
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0.2, 1, 1, 1]),
                   [[np.cos(0.2), -np.sin(0.2), 0, 0],
                    [np.sin(0.2), np.cos(0.2), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    ])
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0.2, 1, 1, 1]),
                   [[np.cos(0.2), -np.sin(0.2), 0, 0],
                    [np.sin(0.2), np.cos(0.2), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    ])
assert np.allclose(params2affine([0, 0, 0, 0, -0.1, 0, 1, 1, 1]),
                   [[np.cos(-0.1), 0, np.sin(-0.1), 0],
                    [0, 1, 0, 0],
                    [-np.sin(-0.1), 0, np.cos(-0.1), 0],
                    [0, 0, 0, 1],
                    ])
assert np.allclose(params2affine([0, 0, 0, 0.3, 0, 0, 1, 1, 1]),
                   [[1, 0, 0, 0],
                    [0, np.cos(0.3), -np.sin(0.3), 0],
                    [0, np.sin(0.3), np.cos(0.3), 0],
                    [0, 0, 0, 1],
                    ])
# Translation
assert np.allclose(params2affine([11, 12, 13, 0, 0, 0, 1, 1, 1]),
                   [[1, 0, 0, 11],
                    [0, 1, 0, 12],
                    [0, 0, 1, 13],
                    [0, 0, 0, 1]
                    ])

#- Make a cost function called `cost_function` that will:
#- * accept the vector of parameters containing x_t ... z_z
#- * generate `P`;
#- * compose template_vox2mm, then P then mm2subject_vox to give `Q`;
#- * resample the subject data using the matrix and vector from `Q`.
#-   Use `order=1` for the resampling - otherwise it will be slow.
#- * return the mismatch metric for the resampled image and template.

#: check the cost function returns the previous value if params
# say to do no transformation
current = correl_mismatch(subject_resampled, template_data)
redone = cost_function([0, 0, 0, 0, 0, 0, 1, 1, 1])
assert np.allclose(current, redone)

#- get fmin_powell

#: a callback we will pass to the fmin_powell function
def my_callback(params):
   print("Trying parameters " + str(params))

#- Call optimizing function and collect best estimates for rotations
#- Collect best estimates in `best_params` variable

#- * compile the P affine from the optimized parameters;
#- * compile the Q affine from the image affines and P;
#- * resample the subject image using the matrix and vector from the Q
#-   affine.

#- show example slice from template and normalized image
