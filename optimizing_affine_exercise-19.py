#- Make a cost function called `cost_function` that will:
#- * accept the vector of parameters containing x_t ... z_z
#- * generate `P`;
#- * compose template_vox2mm, then P then mm2subject_vox to give `Q`;
#- * resample the subject data using the matrix and vector from `Q`.
#-   Use `order=1` for the resampling - otherwise it will be slow.
#- * return the mismatch metric for the resampled image and template.
