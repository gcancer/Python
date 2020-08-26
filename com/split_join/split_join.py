# split
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')
print(arr01)

# [] : list | {} : set, dictionary | () : tuple

arr02 = str01.split(' ', 1) # max split : 몇 개로 자를거냐~
print(arr02)

import re
arr03 = re.split("[\s]|[,]      ",str01)
print(arr03)

# join
arr04 = ['1','2','3','4']
print(arr04)
a = '+'.join(arr04)
print(a)
print(eval(a)) # eval 사용시 주의!

