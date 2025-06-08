import numpy as np

# Create an array with NaN, positive infinity, and negative infinity
data_to_clean = np.array([np.nan, 1, 2, np.nan, np.inf, -np.inf, 3, 4, np.inf, -np.inf])

# Use nan_to_num to replace NaN with 0, positive infinity with a large number, and negative infinity with a small number
cleaned_data = np.nan_to_num(data_to_clean, nan=0.0, posinf=1e6, neginf=-1e6)

print("Original Data:")
print(data_to_clean)
# Output: Original Data:
#         [ nan   1.   2.  nan  inf -inf   3.   4.  inf -inf]

print("\nCleaned Data:")
print(cleaned_data)
# Output: Cleaned Data:
#         [ 0.e+00  1.e+00  2.e+00  0.e+00  1.e+06 -1.e+06  
#           3.e+00  4.e+00  1.e+06  -1.e+06]
