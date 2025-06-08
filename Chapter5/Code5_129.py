import pandas as pd

# Read a .csv file
data = pd.read_csv('hooke.csv')

# Drop the 'Index' column and set it as the index of our dataframe
data = data.set_index('Index')

# Duplicate the original DataFrame
data_stand = data.copy()
data_scal = data.copy()
data_norm = data.copy()

# apply normalization techniques 
# standardization
for column in data_stand.columns: 
    data_stand[column] = (data_stand[column] -
                           data_stand[column].mean()) / data_stand[column].std()
# scaling in range [-1, 1]
for column in data_scal.columns: 
    data_scal[column] = data_scal[column]/ data_scal[column].abs().max()
# normalization 
for column in data_norm.columns: 
    data_norm[column] = (data_norm[column] - data_norm[column].min()) / (data_norm[column].max() - data_norm[column].min())

# Data comparison
print("Original DataFrame:")
print(data)
# Output:  Original DataFrame:
#         "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# Index                                                
# 1              0.00            0.050            0.050
# 2              0.49            0.066            0.066
# 3              0.98            0.087            0.080
# 4              1.47            0.116            0.108
# 5              1.96            0.142            0.138
# 6              2.45            0.166            0.158
# 7              2.94            0.193            0.174
# 8              3.43            0.204            0.192
# 9              3.92            0.226            0.205
# 10             4.41            0.238            0.232

print("\nDataFrame with standardized data:")
print(data_stand)
# Output: DataFrame with standardized data:
#         "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# Index                                                
# 1         -1.486301        -1.467910        -1.446450
# 2         -1.156012        -1.230191        -1.190157
# 3         -0.825723        -0.918186        -0.965902
# 4         -0.495434        -0.487322        -0.517390
# 5         -0.165145        -0.101030        -0.036842
# 6          0.165145         0.255547         0.283523
# 7          0.495434         0.656696         0.539816
# 8          0.825723         0.820128         0.828145
# 9          1.156012         1.146990         1.036382
# 10         1.486301         1.325279         1.468875

print("\nDataFrame with scaled data:")
print(data_scal)
# Output: DataFrame with scaled data:
#         "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# Index                                                
# 1          0.000000         0.210084         0.215517
# 2          0.111111         0.277311         0.284483
# 3          0.222222         0.365546         0.344828
# 4          0.333333         0.487395         0.465517
# 5          0.444444         0.596639         0.594828
# 6          0.555556         0.697479         0.681034
# 7          0.666667         0.810924         0.750000
# 8          0.777778         0.857143         0.827586
# 9          0.888889         0.949580         0.883621
# 10         1.000000         1.000000         1.000000

print("\nDataFrame with normalized data:")
print(data_norm)
# Output: DataFrame with normalized data:
#         "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
# Index                                                
# 1          0.000000         0.000000         0.000000
# 2          0.111111         0.085106         0.087912
# 3          0.222222         0.196809         0.164835
# 4          0.333333         0.351064         0.318681
# 5          0.444444         0.489362         0.483516
# 6          0.555556         0.617021         0.593407
# 7          0.666667         0.760638         0.681319
# 8          0.777778         0.819149         0.780220
# 9          0.888889         0.936170         0.851648
# 10         1.000000         1.000000         1.000000
