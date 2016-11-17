#- Use 'apply_rotations' and the estimated parameters to un-rotate the
#- rotated image
#- Put the new un-rotated image into a variable `best_vol0`
best_vol0 = apply_rotations(rotated_vol0, best_params)
