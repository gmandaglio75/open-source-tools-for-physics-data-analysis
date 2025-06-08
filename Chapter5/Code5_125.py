import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

aggr_functions = data.aggregate({' "Mass (kg)"': ['count', 'mean', 'median', 'min', 'max', 'var', 'std'], ' "Spring 1 (m)"': ['count', 'mean', 'median', 'min', 'max', 'var', 'std'], ' "Spring 2 (m)"': ['count', 'mean', 'median', 'min', 'max', 'var', 'std']})
print(aggr_functions)
# Output:    "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# count      10.000000        10.000000        10.000000
# mean        2.205000         0.148800         0.140300
# median      2.205000         0.154000         0.148000
# min         0.000000         0.050000         0.050000
# max         4.410000         0.238000         0.232000
# var         2.200917         0.004530         0.003897
# std         1.483549         0.067307         0.062429
