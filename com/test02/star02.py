# 1
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))
print('——')

# \n이랑 나머지가 조인 -> '\n'.join('*','**','***','****','*****')

# 나머지 : list 값들이 있다.
# [''.join(['*' for i in range(i + 1)]) for i in range(5)]

# 나머지 리스트 안에 있던 별들
# ''.join(['*' for i in range(i + 1)])
# i가 0일 때 -> ''.join(['*']) -> '*'
# i가 1일 때 -> ''.join(['*', '*']) -> '**'
# ...

# 2
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))
print('——')

# 3
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))
print('——')

# 4
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))
print('——')

# 5
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(2 * i + 1)]) for i in range(5)]))
print('——')