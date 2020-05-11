import numpy as np


# First, create a 4x4 array with arbitrary values, then

a = np.empty((4,4), float)

print(a)

print("\n")

# 1. Extract every element from the second row.

a[1,:] = 2.

print(a)

sec_row = a[1,:]

print(sec_row)

print("\n")

# 2. Extract every element from the third column.

a[:, 2] = 3.

print(a)

third_column = a[:, 2]

print(third_column)

print("\n")

# 3. Assign a value of 0.21 to upper left 2x2 subarray.

a[:2,:2] = .21

print(a)

print("\n")

# Next, create a 8x8 array with checkerboard pattern, i.e. alternating zeros
# and ones:

# 
# 1 0 1 ...
# 0 1 0 ...
# 1 0 1 ...
#  ...
# 


board = np.zeros((8,8), int)

board[0::2,0::2] = 1
board[1::2,1::2] = 1

print(board)