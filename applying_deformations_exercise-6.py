#: get original TPM.nii 3D shape and affine
tpm_shape = deformations_data.shape[:3]
tpm_affine = deformations_img.affine
tpm_affine
# array([[  -1.5,    0. ,    0. ,   90. ],
# [   0. ,    1.5,    0. , -126. ],
# [   0. ,    0. ,    1.5,  -72. ],
# [   0. ,    0. ,    0. ,    1. ]])
