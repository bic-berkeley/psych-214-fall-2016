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

See `rotation in 2D`_ for a visual proof.

*****************************
Rotations in three dimensions
*****************************

Rotations in three dimensions extend simply from two dimensions.  Consider a
`right-handed`_ set of x, y, z axes, maybe forming the x axis with your right
thumb, the y axis with your index finger, and the z axis with your middle
finger.  Now look down the z axis, from positive z toward negative z.  You see
the x and y axes pointing right and up respectively, on a plane in front of
you.  A rotation around z leaves z unchanged, but changes x and y according to
the 2D rotation formula above:

.. math::

   R_z(\theta) &= \begin{bmatrix}
   \cos \theta &  -\sin \theta & 0 \\[3pt]
   \sin \theta & \cos \theta & 0\\[3pt]
   0 & 0 & 1\\
   \end{bmatrix}

For a rotation around x, we look down from positive x to the y and z axes
pointing right and up respectively.  A rotation around x leaves x unchanged
but changes y and z according to the 2D rotation formula:

.. math::

   R_x(\theta) &= \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos \theta &  -\sin \theta \\[3pt]
   0 & \sin \theta  &  \cos \theta \\[3pt]
   \end{bmatrix}

Now consider a rotation around the y axis.   We look from positive y down the
y axis at the other two axes on a plane.  The z axis points up, but the x axis
now points *left* instead of right.  A positive rotation around the y axis now
corresponds to a negative rotation in 2D.  Remembering that $\cos (-\alpha) =
\cos \alpha$ and $\sin (-\alpha) = -\sin \alpha$, we have:

.. math::

   \begin{bmatrix}
   \cos (-\alpha) & -\sin (-\alpha) \\
   \sin (-\alpha) & \cos (-\alpha) \\
   \end{bmatrix} =
   \begin{bmatrix}
   \cos \alpha & \sin \alpha \\
   -\sin \alpha & \cos \alpha \\
   \end{bmatrix}

The formula for a rotation around the y axis in 3D is:

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
