import numpy as np

a = np.array([[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24]])
a
# Output: array([[ 2,  4,  6,  8],
#                [ 10, 12, 14, 16],
#                [ 18, 20, 22, 24]])
print(a)
# Output: [[ 2  4  6  8]
#          [10 12 14 16]
#          [18 20 22 24]]

a.ndim
# Output: 2

print(a.shape)
# Output: (3, 4)
print(type(a.shape))
# Output: <class 'tuple'>
print(a.shape[0])
# Output: 3
print(a.shape[1])
# Output: 4
row, col = a.shape
print(row)
# Output: 3
print(col)
# Output: 4

print(a.size)
# Output: 12
print(type(a.size))
# Output: <class 'int'>
print(a[0].size)
# Output: 4
