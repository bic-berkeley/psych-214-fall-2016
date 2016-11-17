#- Make params2affine function
#- * accepts params vector
#- * builds matrix for zooms
#- * builds atrix for rotations
#- * builds vector for translations
#- * compile into affine and return
def params2affine(params):
    # Unpack the parameter vector to individual parameters
    x_t, y_t, z_t, x_r, y_r, z_r, x_z, y_z, z_z = params
    # Matrix for zooms
    zooms = np.diag([x_z, y_z, z_z])
    # Matrix for rotations
    x_rot = x_rotmat(x_r)
    y_rot = y_rotmat(y_r)
    z_rot = z_rotmat(z_r)
    # Vector for translations
    vec = [x_t, y_t, z_t]
    # Build into affine
    mat = x_rot.dot(y_rot).dot(z_rot).dot(zooms)
    return nib.affines.from_matvec(mat, vec)
