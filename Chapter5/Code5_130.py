import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

# Drop the 'Index' column and set it as the index of our dataframe
data_set_index = data.set_index('Index')

# Filter the data considering all the mass values between 1 and 4 
row_filter = data_set_index[
    ((data_set_index[' "Mass (kg)"'] >= 1) & (data_set_index[' "Mass (kg)"'] <= 4))
    ]
print(row_filter)
# Output: "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# Index                                                
# 4              1.47            0.116            0.108
# 5              1.96            0.142            0.138
# 6              2.45            0.166            0.158
# 7              2.94            0.193            0.174
# 8              3.43            0.204            0.192
# 9              3.92            0.226            0.205
