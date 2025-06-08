import numpy as np

# Sample dataset: time readings from several stopwatches (in seconds)
recorded_times = np.array([5.0, 3.1, 7.2, 3.3, 8.4, 2.5, 4.2, 3.8, 9.1, 3.9])
print("Time readings:")
print(recorded_times)
# Output: Time readings:
#         [5.  3.1 7.2 3.3 8.4 2.5 4.2 3.8 9.1 3.9]

# From "recorded_times" we want to select only times greater than 4 seconds
print('\nFrom "Time readings", we want to select only times greater than 4 seconds.')
# Output: From "Time readings", we want to select only times greater than 4 seconds.

# Method 1. Filter values by constructing a list of indices to use as a selector
indices = [0, 2, 4, 6, 8]
method1 = recorded_times[indices]
print("\nFiltering with method 1 (indices):")
print(method1)
# Output: Filtering with method 1 (indices):
#         [5.  7.2 8.4 4.2 9.1]

# Method 2. Filter values by constructing a list of True and False (boolean array)
boolean_array = [True, False, True, False, True, False, True, False, True, False]
method2 = recorded_times[boolean_array]
print("\nFiltering with method 2 (boolean array):")
print(method2)
# Output: Filtering with method 2 (boolean array):
#         [5.  7.2 8.4 4.2 9.1]

# Method 3. Filter array based on conditions
filtered_arr = []
# go through each element in arr
for element in recorded_times:
    # if the element is higher than 4, set the value to True, otherwise False:
    if element > 4:
        filtered_arr.append(True)
    else:
        filtered_arr.append(False)
method3 = recorded_times[filtered_arr]
print("\nFiltering with method 3 (filter array with conditions):")
print(method3)
# Output: Filtering with method 3 (filter array with conditions):
#         [5.  7.2 8.4 4.2 9.1]

# Method 4. Filter array with iterable variable in our condition
mask = recorded_times > 4
method4 = recorded_times[mask]
print("\nFiltering with method 4 (filter array with iterable variable):")
print(method4)
# Output: Filtering with method 4 (filter array with iterable variable):
#         [5.  7.2 8.4 4.2 9.1]

