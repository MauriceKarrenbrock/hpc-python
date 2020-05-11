"""
Create a new 8x8 array with some values (or continue with the one created in
the [Array slicing](../array-slicing) exercise).

1. Use `np.split()` function for splitting the array into two new 4x8 arrays.
   Reconstruct the original 8x8 array by using `np.concatenate()`.
2. Repeat the above exercise but create now 8x4 subarrays and then combine
   them.
"""

import numpy as np

a = np.arange(64).reshape(8,8)

split_1 = np.split(a, 2)

new_a = np.concatenate(split_1)

print (split_1)

print("\n")

print(a == new_a)

print("\n")

split_2 = np.split(a, 2, axis = 1)

new_a = np.concatenate(split_2, axis = 1)

print (split_2)

print("\n")

print(a == new_a)




