import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

# Drop the 'Index' column and set it as the index of our dataframe
data_set_index = data.set_index('Index')
print("\nDataFrame after dropping 'Index' column and set it as the index of our dataframe:")
print(data_set_index)

print("\nAccess a record:")
print(data_set_index.loc[1])
# Output: "Mass (kg)"       0.00
#         "Spring 1 (m)"    0.05
#         "Spring 2 (m)"    0.05
print(data_set_index.iloc[0])
# Output: "Mass (kg)"       0.00
#         "Spring 1 (m)"    0.05
#         "Spring 2 (m)"    0.05
