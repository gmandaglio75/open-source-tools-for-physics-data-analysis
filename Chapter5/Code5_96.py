import numpy as np

a = np.array([2, 4, 6, 8, 10])

#Slicing
v = a[2:]
v
# Output: array([6, 8, 10])
v[0] = 1
a
# Output: array([ 2,  4,  1, 8, 10])
