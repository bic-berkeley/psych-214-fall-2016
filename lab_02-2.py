# Open a file in Read Binary mode to read bytes
fobj = open('our_paper.txt', 'rb')
# Read contents as bytes
contents = fobj.read()  # Read the whole file
fobj.close()
type(contents)
# <class 'bytes'>
