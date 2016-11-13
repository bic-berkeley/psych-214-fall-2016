#- Make apply_rotations function, accepting `vol_arr` and `rotations`
#- vector, returning image with rotations applied.
def apply_rotations(vol_arr, rotations):
    r_x, r_y, r_z = rotations
    rotation_matrix = z_rotmat(r_z).dot(y_rotmat(r_y)).dot(x_rotmat(r_x))
    # apply rotations to make new image
    # return new image
    return affine_transform(vol_arr, rotation_matrix, order=1)
