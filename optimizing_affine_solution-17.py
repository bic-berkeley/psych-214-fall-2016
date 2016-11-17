#- Make a cost function called `cost_function` that will:
#- * accept the vector of parameters containing x_t ... z_z
#- * generate `P`;
#- * compose template_vox2mm, then P then mm2subject_vox to give `Q`;
#- * resample the subject data using the matrix and vector from `Q`.
#-   Use `order=1` for the resampling - otherwise it will be slow.
#- * return the mismatch metric for the resampled image and template.
def cost_function(params):
    P = params2affine(params)
    Q = npl.inv(subject_img.affine).dot(P).dot(template_img.affine)
    mat,  vec = nib.affines.to_matvec(Q)
    resampled = affine_transform(subject_data, mat, vec,
                                 output_shape=template_img.shape,
                                 order=1)
    return correl_mismatch(template_data, resampled)
