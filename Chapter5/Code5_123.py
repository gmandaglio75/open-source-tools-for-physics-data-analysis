import pandas as pd

# Read a .csv file
data = pd.read_csv('...\hooke.csv')

# Define new data for additional columns
spring_3 = [0.060, 0.074, 0.088, 0.116, 0.146, 0.166, 0.182, 0.200, 0.213, 0.240]
spring_4 = [0.061, 0.073, 0.084, 0.115, 0.141, 0.161, 0.187, 0.205, 0.211, 0.246]

# Add multiple columns using dictionary assignment
new_data = {'"Spring 3 (m)"': spring_3, '"Spring 4 (m)"': spring_4 }
data = data.assign(**new_data)
