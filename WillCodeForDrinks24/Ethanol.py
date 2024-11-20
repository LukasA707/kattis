n = int(input())

x = 4 + 2*n
output = [[' ' for _ in range(x)] for _ in range(5)]

#   0 1 2 3 4 5 6 7 
# 0     H   H
# 1     |   |
# 2 H - C - C - O H
# 3     |   |
# 4     H   H

#Prepend

output[2][0] = 'H'
output[2][1] = '-'

# Dynamic by n

for i in range(0,2*n,2):
    output[0][2+i] = 'H'
    output[1][2+i] = '|'
    output[2][2+i] = 'C'
    output[3][2+i] = '|'
    output[4][2+i] = 'H'
    output[2][3+i] = '-'

# Append

output[2][2+2*n] = 'O'
output[2][3+2*n] = 'H'

for i in range(5):
    for j in range(x):
        print(output[i][j], end='', sep='')
    print()