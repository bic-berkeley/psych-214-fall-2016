#- Make a 3 by 3 transformation matrix that applies this sequence
#- * 0.1 radians around the x axis, then
#- * 0.2 radians around the y axis, then
#- * 0.3 radians around the z axis.
M = z_rotmat(0.3).dot(y_rotmat(0.2)).dot(x_rotmat(0.1))
M
# array([[ 0.9363, -0.2751,  0.2184],
# [ 0.2896,  0.9564, -0.037 ],
# [-0.1987,  0.0978,  0.9752]])
