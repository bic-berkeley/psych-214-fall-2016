#: voxels in TPM.nii to voxels in mni_icbm152_t1_tal_nlin_asym_09a.nii
# Matrix multiplication is right to left
vox2vox = npl.inv(template_img.affine).dot(tpm_affine)
vox2vox
# array([[  -1.5,    0. ,    0. ,  188. ],
# [   0. ,    1.5,    0. ,    8. ],
# [   0. ,    0. ,    1.5,    0. ],
# [   0. ,    0. ,    0. ,    1. ]])
