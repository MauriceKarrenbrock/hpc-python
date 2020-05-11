# A simple method for evaluating integrals numerically is by the middle Riemann
# sum

# <!--- Equation
# S = \int_a^b f(x) dx = \sum_{i=1}^n f(x'_i) \Delta x
# --->

# ![img](https://quicklatex.com/cache3/e2/ql_30419670e67bc2b3d039e8a9d8653de2_l3.png)

# with

# <!--- Equation
# x'_i = (x_i + x_{i-1}) / 2; x_0 = a, x_n = b
# --->

# ![img](https://quicklatex.com/cache3/09/ql_f124fd5c831e873c6abd41160fae2d09_l3.png)

# Calculate the integral in the interval [0,π/2] and investigate how much the
# Riemann sum of **sin** differs from 1.0. Avoid `for` loops. Investigate also
# how the results changes with the choice of Δx.


import numpy as np

delta = (1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001)

for i in delta:

    x_values = np.arange(0, (np.pi / 2.) + i, i)

    integral_value = np.sum( np.sin((x_values[1:] + x_values[:-1]) / 2.) * i )
    
    print(integral_value - 1.)