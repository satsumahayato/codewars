# 8 Kyu
# Beginner Series #1 School Paperwork
# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python

<<<<<<< HEAD
# Your classmates asked you to copy some paperwork for them.
# You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need.

=======
>>>>>>> d3a086ea9a0f65b8775543028408a2b6808ce113
def paperwork(n, m):
    if (n < 0) or (m < 0):
        return 0
    else:
        return (n * m)
