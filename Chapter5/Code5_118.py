import pandas as pd

# Data
names = ['Sebastiano', 'Giuseppe', 'Ulderico']
ages = [36, 48, 64]

# Create a Series
name_series = pd.Series(ages, index=names)

# Display the Series
print("Name and Age Series:")
print(name_series)
# Output: Name and Age Series:
#         Sebastiano    36
#         Giuseppe      48
#         Ulderico      64
#         dtype: int64
