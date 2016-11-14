#- * compile the P affine from the optimized parameters;
#- * compile the Q affine from the image affines and P;
#- * resample the subject image using the matrix and vector from the Q
#-   affine.
P = params2affine(best_params)
Q = npl.inv(subject_img.affine).dot(P).dot(template_img.affine)
mat, vec = nib.affines.to_matvec(Q)
best_subject_data = affine_transform(subject_data, mat, vec,
                                     output_shape=template_img.shape)
