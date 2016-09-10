#: This function uses matplotlib 3D plotting and sckit-image for rendering
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure
# >>>
def binarized_surface(binary_array):
    """ Do a 3D plot of the surfaces in a binarized image
# ...
    This uses scikit-image and some fancy commands that we don't
    need to worry about at the moment, to do the plot.
    """
    verts, faces = measure.marching_cubes(binary_array, 0)
    fig = plt.figure(figsize=(10, 12))
    ax = fig.add_subplot(111, projection='3d')
# ...
    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], linewidths=0, alpha=0.5)
    ax.add_collection3d(mesh)
    ax.set_xlim(0, binary_array.shape[0])
    ax.set_ylim(0, binary_array.shape[1])
    ax.set_zlim(0, binary_array.shape[2])
