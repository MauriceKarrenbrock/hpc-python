"""
File [xy-coordinates.dat](xy-coordinates.dat) contains a list of (x,y) value
pairs. Read the data with `numpy.loadtxt()`. Add then 2.5 to all y values and
write the new data into a file using `numpy.savetxt()`.
"""

import numpy as np

data = np.loadtxt("xy-coordinates.dat")

data[:, 1] = data[:, 1] + 2.5

np.savetxt("new_file.dat", data, fmt = "%5.5f")

