fobj = open("/tmp/important_notes.txt", "rt")
lines = fobj.readlines()
fobj.close()
len(lines)
# 2
print(lines[0])
# captains log 672828: I had a banana for breakfast.
# <BLANKLINE>
print(lines[1])
# captains log 672829: I should watch less TV.
# <BLANKLINE>
