# Vectorization is crucial for obtaining good performance with NumPy.

# Derivatives can be calculated numerically with the finite-difference method
# as:

# <!--- Equation
# f'(x_i) = \frac{f(x_i + \Delta x)- f(x_i - \Delta x)}{2 \Delta x}
# --->

# ![img](https://quicklatex.com/cache3/0a/ql_d10c99a114e66c7ed0535e0aeb041d0a_l3.png)

# Construct 1D Numpy array containing the values of xi in the interval [0,π/2]
# with spacing Δx=0.1. Evaluate numerically the derivative of **sin** in this
# interval (excluding the end points) using the above formula. Try to avoid
# `for` loops. Compare the result to function **cos** in the same interval.

import numpy as np

input_values = np.arange(0., (np.pi / 2.) + .1, .1)

d_sin = np.empty(input_values.size - 2, float)

d_sin[:] = (np.sin(input_values[2:]) - np.sin(input_values[:-2])) / (2. * .1)

diff = np.empty(input_values.size - 2, float)

diff[:] = d_sin[:] - np.cos(input_values[:-2])

print("d sin\n")

print(d_sin)

print("\ndiff\n")

print(diff)