my_file2 = open("a_text_file.txt", "rt")
for line in my_file2:  # iterating over the file object
    print("Line is:", line)
# ...
# Line is: MATLAB is good for matrices
# <BLANKLINE>
# Line is: Python is good for coding
# <BLANKLINE>
my_file2.close()
