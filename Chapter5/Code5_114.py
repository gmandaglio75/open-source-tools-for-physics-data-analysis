import numpy as np

# Sample dataset: voltage readings from different sensors (in volts)
voltage = np.array([2.5, 3.6, 1.8, 4.5, 3.1, 2.9, 1.7, 2.0, 3.4, 1.5])

# Calculate the minimum and maximum values
min_val = np.min(voltage)
max_val = np.max(voltage)

# Scale the dataset to the range [0, 1]
scaled_voltage = (voltage - min_val) / (max_val - min_val)

print("Original Data (Volts):")
print(voltage)
# Output: Original Data (Volts):
#         [2.5 3.6 1.8 4.5 3.1 2.9 1.7 2.  3.4 1.5]

print("\nScaled Data [0, 1]:")
print(scaled_voltage)
# Output: Scaling Data:
#         [0.33333333 0.7        0.1        1.         0.53333333 
#          0.46666667  0.06666667 0.16666667 0.63333333 0.        ]
