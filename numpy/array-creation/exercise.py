import numpy as np

#1. Start from a Python list containing both integers and floating point values,
#and construct then a NumPy array from the list.

float_integer_list = [1, 2, 3.3, 55.E-20, 500]

float_integer_array = np.array(float_integer_list)

print(type(float_integer_array))
print(float_integer_array)
print(float_integer_array.shape)
print(float_integer_array.size)


# 2. Generate a 1D NumPy array containing all numbers from -2.0 to 2.0 with a
# spacing of 0.2. Use optional start and step arguments of the `np.arange()`
# function.

one_d_array = np.arange(-2., 2. + .2, .2)

print(one_d_array)

# 3. Generate another 1D NumPy array containing 11 equally spaced values between
# 0.5 and 1.5. 

equal_spaced_array = np.linspace(.5, 1.5, 11)

print(equal_spaced_array)

# 4. Take some Python string and construct from it NumPy array consisting of 
# single characters (a character array).

string = "ABCabc"

char_array = np.array(string, dtype = 'c')

print(char_array)