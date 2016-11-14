numbers = [1.2, 2.3, 3.4, 4.5]
fobj = open('some_numbers.txt', 'wt')
for number in numbers:
    # String version of number, plus end-of-line character
    fobj.write(str(number) + '\n')
# 4
# 4
# 4
# 4
fobj.close()
