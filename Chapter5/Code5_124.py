import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

# Get summary statistics
print(data.describe())
# Output:   Index   "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# count  10.00000     10.000000        10.000000        10.000000
# mean    5.50000      2.205000         0.148800         0.140300
# std     3.02765      1.483549         0.067307         0.062429
# min     1.00000      0.000000         0.050000         0.050000
# 25%     3.25000      1.102500         0.094250         0.087000
# 50%     5.50000      2.205000         0.154000         0.148000
# 75%     7.75000      3.307500         0.201250         0.187500
# max    10.00000      4.410000         0.238000         0.232000
