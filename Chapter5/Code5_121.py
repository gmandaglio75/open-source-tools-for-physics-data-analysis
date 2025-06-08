import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')
print(data.head())
# Output:  Index   "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
#       0      1          0.00            0.050            0.050
#       1      2          0.49            0.066            0.066
#       2      3          0.98            0.087            0.080
#       3      4          1.47            0.116            0.108
#       4      5          1.96            0.142            0.138
