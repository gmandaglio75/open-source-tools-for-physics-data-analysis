import numpy as np

a = np.array([2, 4, 6, 8, 10])

#Indexing
a[0]
# Output: 2
a[:3]
# Output: array([2, 4, 6])

#Variability
a[0] = 11
a
# Output: array([11, 4, 6, 8, 10])
