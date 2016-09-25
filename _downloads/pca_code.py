""" PCA exercise
"""

#: import common modules
import numpy as np  # the Python array package
import matplotlib.pyplot as plt  # the Python plotting package
# Display array values to 6 digits of precision
np.set_printoptions(precision=4, suppress=True)

#- import numpy.linalg with a shorter name

#- Load the image 'ds114_sub009_t2r1.nii' with nibabel
#- Get the data array from the image

#- Make variables:
#- 'vol_shape' for shape of volumes
#- 'n_vols' for number of volumes

#- Slice the image data array to give array with only first two
#- volumes

#- Set N to be the number of voxels in a volume

#- Reshape to 2D array with first dimension length N

#- Transpose to 2 by N array

#- Calculate the mean across columns

#- Row means copied N times to become a 2 by N array

#- Subtract the means for each row, put the result into X
#- Show the means over the columns, after the subtraction

#- Plot the signal in the first row against the signal in the second

#- Calculate unscaled covariance matrix for X

#- Use SVD to return U, S, VT matrices from unscaled covariance

#- Show that the columns in U each have vector length 1

#- Confirm orthogonality of columns in U

#- Show the total sum of squares in X
#- Is this (nearly) the same as the sum of the values in S?

#- Plot the signal in the first row against the signal in the second
#- Plot line corresponding to a scaled version of the first principal component
#- (Scaling may need to be negative)

#- Calculate the projection coefficients for projecting X onto the vectors in U
#- Put the result into a new array C.

#- Transpose C
#- Reshape the first dimension of C to have the 3D shape of the
#- original data volumes.

#- Break 4D array into two 3D volumes

#- Show middle slice (over third dimension) from volume of coefficients
#- for first component

#- Show middle slice (over third dimension) from volume of coefficients
#- for second component

#- Reshape first dimension of whole image data array to N, and take
#- transpose

#- Calculate mean across columns
#- Expand to (173, N) shape using np.outer
#- Subtract from data array to remove mean over columns (row means)
#- Put result into array X

#- Calculate unscaled covariance matrix of X


#- Use subplots to make axes to plot first 10 principle component
#- vectors
#- Plot one component vector per sub-plot.

#- Calculate scalar projection coefficients for projecting X onto U
#- Put results into array C.

#- Transpose C
#- Reshape the first dimension of C to have the 3D shape of the
#- original data volumes.

#- Show middle slice (over third dimension) of first principal
#- component volume

#- Make the mean volume (mean over the last axis)
#- Show the middle slice (slicing over the third axis)

#- Show middle slice (over third dimension) of second principal
#- component volume

#- Show middle slice (over third dimension) of third principal
#- component volume
