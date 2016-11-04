from os.path import abspath
# Show the current working directory
os.getcwd()  #doctest: +SKIP
# /Users/mb312/dev_trees/psych-214-fall-2016
abspath('relative/path/then_filename.txt')  #doctest: +SKIP
# /Users/mb312/dev_trees/psych-214-fall-2016/relative/path/then_filename.txt
