###############################
Rotations and rotation matrices
###############################

***************************
Rotations in two dimensions
***************************

See: `rotation in 2d`_.

In two dimensions, rotating a vector :math:`\theta` around the origin can be
expressed as a 2 by 2 transformation matrix:

.. math::

   R(\theta) = \begin{bmatrix}
   \cos \theta & -\sin \theta \\
   \sin \theta & \cos \theta \\
   \end{bmatrix}

This matrix rotates column vectors by matrix multiplication on the left:

.. math::

   \begin{bmatrix}
   x' \\
   y' \\
   \end{bmatrix} = \begin{bmatrix}
   \cos \theta & -\sin \theta \\
   \sin \theta & \cos \theta \\
   \end{bmatrix}\begin{bmatrix}
   x \\
   y \\
   \end{bmatrix}

The coordinates :math:`(x',y')` of the point :math:`(x,y)` after rotation are:

.. math::

   x' = x \cos \theta - y \sin \theta \\
   y' = x \sin \theta + y \cos \theta

See `rotations in 2D`_ for a visual proof.

*****************************
Rotations in three dimensions
*****************************

Rotations in three dimensions extend simply from two dimeions. For example, in
3D, the rotation above would be a rotation around the z axis (z stays
constant, x and y change):

.. math::

   R_z(\theta) &= \begin{bmatrix}
   \cos \theta &  -\sin \theta & 0 \\[3pt]
   \sin \theta & \cos \theta & 0\\[3pt]
   0 & 0 & 1\\
   \end{bmatrix}

For a rotation around the x axis, x stays the same, y and z change:

.. math::

   R_x(\theta) &= \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos \theta &  -\sin \theta \\[3pt]
   0 & \sin \theta  &  \cos \theta \\[3pt]
   \end{bmatrix}

There is a sign flip for the rotation around the y axis.  This is to do with
the direction of the rotation relative to the direction (positive to negative)
of the axes.  You may be able to persuade yourself of this by drawing the x,
y, z axes and thinking about the rotation around the y axis when observing
from the positive end of the y axis:

.. math::

   R_y(\theta) &= \begin{bmatrix}
   \cos \theta & 0 & \sin \theta \\[3pt]
   0 & 1 & 0 \\[3pt]
   -\sin \theta & 0 & \cos \theta \\
   \end{bmatrix}

We can combine rotations with matrix multiplication. For example, here is an
rotation of $\gamma$ radians around the x axis:

.. math::

   \begin{bmatrix}
   x'\\
   y'\\
   z'\\
   \end{bmatrix} =
   \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos(\gamma) & -\sin(\gamma) \\
   0 & \sin(\gamma) & \cos(\gamma) \\
   \end{bmatrix}
   \begin{bmatrix}
   x\\
   y\\
   z\\
   \end{bmatrix}

We could then apply a rotation of $\phi$ radians around the y axis:

.. math::

   \begin{bmatrix}
   x''\\
   y''\\
   z''\\
   \end{bmatrix} =
   \begin{bmatrix}
   \cos(\phi) & 0 & \sin(\phi) \\
   0 & 1 & 0 \\
   -\sin(\phi) & 0 & \cos(\phi) \\
   \end{bmatrix}
   \begin{bmatrix}
   x'\\
   j'\\
   k'\\
   \end{bmatrix}

We could also write the combined rotation as:

.. math::

   \begin{bmatrix}
   x''\\
   y''\\
   z''\\
   \end{bmatrix} =
   \begin{bmatrix}
   \cos(\phi) & 0 & \sin(\phi) \\
   0 & 1 & 0 \\
   -\sin(\phi) & 0 & \cos(\phi) \\
   \end{bmatrix}
   \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos(\gamma) & -\sin(\gamma) \\
   0 & \sin(\gamma) & \cos(\gamma) \\
   \end{bmatrix}
   \begin{bmatrix}
   x\\
   y\\
   z\\
   \end{bmatrix}

Because matrix multiplication is associative:

.. math::

   \mathbf{Q} = \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos(\gamma) & -\sin(\gamma) \\
   0 & \sin(\gamma) & \cos(\gamma) \\
   \end{bmatrix}

.. math::

   \mathbf{P} = \begin{bmatrix}
   \cos(\phi) & 0 & \sin(\phi) \\
   0 & 1 & 0 \\
   -\sin(\phi) & 0 & \cos(\phi) \\
   \end{bmatrix}

.. math::

   \mathbf{M} = \mathbf{P} \cdot \mathbf{Q}

.. math::

   \begin{bmatrix}
   x''\\
   y''\\
   z''\\
   \end{bmatrix} =
   \mathbf{M}
   \begin{bmatrix}
   x\\
   y\\
   z\\
   \end{bmatrix}

:math:`\mathbf{M}` is the rotation matrix that encodes a rotation by
:math:`\gamma` radians around the x axis *followed by* a rotation by
:math:`\phi` radians around the y axis.  We know that the y axis rotation
follows the x axis rotation because matrix multiplication operates from right
to left.
