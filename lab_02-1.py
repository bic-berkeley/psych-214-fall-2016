# Open the file in Read Binary mode
fobj = open('ds107_sub001_highres.nii', 'rb')
# Read contents as bytes
contents = fobj.read()  # Read the whole file
fobj.close()
type(contents)
# <class 'bytes'>
