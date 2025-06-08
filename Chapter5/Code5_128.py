import pandas as pd

# Create a sample DataFrame
data = {
    'Time (minutes)': [0, 10, 20, 30, 40],
    'Temperature (C)': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Use .transform() to apply the conversion function to the temperature data
df['Temperature (F)'] = df['Temperature (C)'].transform(celsius_to_fahrenheit)

print(df)
# Output:  Time (minutes)  Temperature (C)  Temperature (F)
# 0                     0               20             68.0
# 1                    10               25             77.0
# 2                    20               30             86.0
# 3                    30               35             95.0
# 4                    40               40            104.0	
