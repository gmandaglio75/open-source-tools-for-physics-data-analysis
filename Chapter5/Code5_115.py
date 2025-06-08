import numpy as np

# Sample dataset: voltage readings from different sensors (in volts)
voltage = np.array([2.5, 3.6, 1.8, 4.5, 3.1, 2.9, 1.7, 2.0, 3.4, 1.5])

# Calculate the L2 norm of the dataset
l2_norm = np.linalg.norm(voltage)

# Normalize the dataset
normalized_data = voltage / l2_norm

print("Original Data (Volts):")
print(voltage)
# Output: Original Data (Volts):
#         [2.5 3.6 1.8 4.5 3.1 2.9 1.7 2.  3.4 1.5]

print("\nL2 norm:")
print(l2_norm)
# Output: L2 norm:
#         9.023303164584464

print("\nNormalized Data:")
print(normalized_data)
# Output: Normalized Data:
#         [0.2770604  0.39896698 0.19948349 0.49870872 
#          0.3435549  0.32139007 0.18840107 0.22164832 
#          0.37680215 0.16623624]
