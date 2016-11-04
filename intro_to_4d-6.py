fobj = open('some_numbers.txt', 'rt')
numbers_again = []
for line in fobj.readlines():
    numbers_again.append(float(line))
numbers_again
# [1.2, 2.3, 3.4, 4.5]
