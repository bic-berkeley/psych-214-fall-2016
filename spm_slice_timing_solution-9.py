#: import the routines for working with the operating system
import os
# Delete file if it exists
if os.path.exists('afds114_sub009_t2r1.nii'):
    os.unlink('afds114_sub009_t2r1.nii')  # delete file
