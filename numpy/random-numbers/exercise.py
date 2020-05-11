"""
Generate a one dimensional 1000 element array of uniformly distributed random
numbers using the `numpy.random` module.

1. Calculate the mean and standard deviation of the array using `numpy.mean()`
   and `numpy.std()`.
2. Choose some other random distribution and calculate its mean and standard
   deviation.

You can visualize the random distributions with matplotlib’s `hist()`
function.
"""

import numpy as np

import matplotlib.pyplot as plt

a = np.random.uniform(size=1000)

plt.hist(a)

print(f"mean\n{np.mean(a)}\n\n\n\ndev\n{np.std(a)}\n\n\n")

b = np.random.normal((1000))

#plt.hist(b)

print(f"mean\n{np.mean(b)}\n\n\n\ndev\n{np.std(b)}\n\n\n")

c = np.random.random((1000))

#plt.hist(c)

print(f"mean\n{np.mean(c)}\n\n\n\ndev\n{np.std(c)}\n\n\n")


plt.show()
