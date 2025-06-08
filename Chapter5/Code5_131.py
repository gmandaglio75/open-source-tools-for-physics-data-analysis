import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

# Drop the 'Index' column and set it as the index of our dataframe
data_set_index = data.set_index('Index')

# Select only the ' "Spring 1 (m)"' and ' "Spring 2 (m)"' columns
columns_filter = data_set_index[[' "Spring 1 (m)"', ' "Spring 2 (m)"']]
print(columns_filter)
# Output:  "Spring 1 (m)"   "Spring 2 (m)"
# Index                                  
# 1                 0.050            0.050
# 2                 0.066            0.066
# 3                 0.087            0.080
# 4                 0.116            0.108
# 5                 0.142            0.138
# 6                 0.166            0.158
# 7                 0.193            0.174
# 8                 0.204            0.192
# 9                 0.226            0.205
# 10                0.238            0.232
