#- Make a cost function, that
#- * is called 'cost_function'
#- * accepts a vector of rotations as input
#- * applies the vector of rotations to `rotated_vol0` from the global
#-   scope
#- * returns the mismatch metric for the transformed copy of
#-   `rotated_vol0` and `vol0`
def cost_function(rotations):
    Y_t = apply_rotations(rotated_vol0, rotations)
    return correl_mismatch(vol0, Y_t)
