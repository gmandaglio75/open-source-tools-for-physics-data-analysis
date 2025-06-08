import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

# Using DataFrame.insert() to add a column
data.insert(4, "Spring 3 (m)", [0.060, 0.074, 0.088, 0.116, 0.146, 0.166, 0.182, 0.200, 0.213, 0.240], True)

#Save the data with .to_csv()
data.to_csv('hooke_new.txt')
