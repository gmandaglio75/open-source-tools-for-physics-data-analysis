import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

print("Original DataFrame:")
print(data)
# Output: Original DataFrame:
#    Index   "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# 0      1          0.00            0.050            0.050
# 1      2          0.49            0.066            0.066
# 2      3          0.98            0.087            0.080
# 3      4          1.47            0.116            0.108
# 4      5          1.96            0.142            0.138
# 5      6          2.45            0.166            0.158
# 6      7          2.94            0.193            0.174
# 7      8          3.43            0.204            0.192
# 8      9          3.92            0.226            0.205
# 9     10          4.41            0.238            0.232

# Drop a column
data_dropped_column = data.drop('Index', axis=1)
print("\nDataFrame after dropping 'Index' column:")
print(data_dropped_column)
# Output: DataFrame after dropping 'Index' column:
#     "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# 0          0.00            0.050            0.050
# 1          0.49            0.066            0.066
# 2          0.98            0.087            0.080
# 3          1.47            0.116            0.108
# 4          1.96            0.142            0.138
# 5          2.45            0.166            0.158
# 6          2.94            0.193            0.174
# 7          3.43            0.204            0.192
# 8          3.92            0.226            0.205
# 9          4.41            0.238            0.232
