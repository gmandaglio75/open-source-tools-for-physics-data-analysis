import numpy as np

# Sample dataset: modules of the acceleration vector
acceleration = np.array([2.5, 3.6, -4.5, -1.2, 1.1, 2.9, 1.7, 2.0, 3.4, -1.5])

# Calculate the absolute and maximum values
abs_val = np.abs(acceleration)
max_abs_val = np.max(abs_val)

# Scale the dataset to the range [-1, 1]
scaled_acceleration = acceleration / max_abs_val

print("Original Data:")
print(acceleration)
# Output: Original Data:
#         [ 2.5  3.6 -4.5 -1.2  1.1  2.9  1.7  2.   3.4 -1.5]

print("\nScaled Data [-1, 1]:")
print(scaled_acceleration)
# Output: Scaled Data [-1, 1]:
#         [ 0.55555556  0.8        -1.         -0.26666667  
#           0.24444444  0.64444444  0.37777778  0.44444444  
#           0.75555556  -0.33333333]
