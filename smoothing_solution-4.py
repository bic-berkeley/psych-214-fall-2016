#: get first volume from functional
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
vol0 = data[..., 0]
