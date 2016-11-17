mat, vec = to_matvec(zooms_plus_translations)
mat.dot(points.T).T + vec.reshape((1, 3))
# array([[11, 16, 23],
# [17, 20, 33],
# [20,  4, 18],
# [26, 24, 18]])
