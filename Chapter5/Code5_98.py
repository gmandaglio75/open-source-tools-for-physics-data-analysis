import numpy as np

# Example data (fall times of an object)
fall_times = np.array([1.2, 1.5, 1.8, 1.4, 1.6])

# Calculate the mean
mean_fall_time = np.mean(fall_times)
print(f"Mean fall time = {mean_fall_time:.2f} seconds")
# Output: Mean fall time = 1.50 seconds
