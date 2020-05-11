"""
NumPy broadcasting is powerful tool for dealing with different, but compatible
shape arrays.

File [points_circle.dat](points_circle.dat) contains x, y coordinates along a
circle. Translate all the coordinates with some vector e.g. (2.1, 1.1). Plot
both the original and translated points in order to see the effect of
translation.

In case you are not familiar with `matplotlib`, below is a simple example for
plotting coordinates:

~~~python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
y = np.random.random(10)
plt.plot(x, y, 'o')
plt.show()
~~~
"""

import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('points_circle.dat')

vector = np.array((2.1, 1.1))

translated = data + vector

x_1 = data[:,0]
y_1 = data[:,1]

plt.plot(x_1, y_1, "o")


x_2 = translated[:,0]
y_2 = translated[:,1]

plt.plot(x_2, y_2, "d")

plt.show()