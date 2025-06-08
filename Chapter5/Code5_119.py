import pandas as pd

# Create a simple DataFrame
data = {'names': ['Sebastiano', 'Giuseppe', 'Ulderico'],
        'ages': [36, 48, 64]}
df = pd.DataFrame(data)
print(df)
# Output:    names  ages
# 0     Sebastiano    36
# 1       Giuseppe    48
# 2       Ulderico    64
