import numpy as np

# Sample dataset: temperature readings from different sensors (in Celsius)
temperatures = np.array([14.8, 15.2, 16.8, 14.5, 17.1, 15.9, 16.3, 17.0, 15.4, 16.1])

# Calculate the mean and standard deviation
mean = np.mean(temperatures)
std_dev = np.std(temperatures)

# Standardize the dataset
standardized_temperatures = (temperatures - mean) / std_dev

print("Original Data (Celsius):")
print(temperatures)
# Output: Original Data (Celsius):
#         [14.8 15.2 16.8 14.5 17.1 15.9 16.3 17.  15.4 16.1]

print("\nStandardized Data:")
print(standardized_temperatures)
# Output: Standardized Data:
#         [-1.27586207 -0.81609195  1.02298851 -1.62068966  1.36781609 
#          -0.01149425   0.44827586  1.25287356 -0.5862069   0.2183908 ]

# Checking the validity of the standardization procedure carried out
print("Mean of standardized temperatures:")
print(np.mean(standardized_temperatures))
# Output: Mean of standardized temperatures: 4.468647674116255e-16

print("\nStandard deviation of standardized temperatures:")
print(np.std(standardized_temperatures))
# Output: Standard deviation of standardized temperatures: 1.0

