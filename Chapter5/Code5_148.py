import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Read a .csv file
data = pd.read_csv('hooke.csv')

x = data[' "Mass (kg)"']
y1 = data[' "Spring 1 (m)"']
y2 = data[' "Spring 2 (m)"']

result1 = stats.linregress(x, y1)
result2 = stats.linregress(x, y2)

slope1 = result1.slope
intercept1 = result1.intercept
fit1 = intercept1 + slope1 * x
slope2 = result2.slope
intercept2 = result2.intercept
fit2 = intercept2 + slope2 * x

print(f"R-squared for Spring #1: {result1.rvalue**2:.6f}")
print(f"R-squared for Spring #2: {result2.rvalue**2:.6f}")

# Output:    
# R-squared for Spring #1: 0.991265
# R-squared for Spring #2: 0.992243

# Plot data in the same graph
ax1 = plt.scatter(x, y1, label='Spring 1')
ax2 = plt.plot(x, fit1, 'b', label='Fit - Spring 1')
ax3 = plt.scatter(x, y2, label='Spring 2')
ax4 = plt.plot(x, fit2, 'r', label='Fit - Spring 2')

k1 = 9.81/result1.slope
k2 = 9.81/result2.slope

print(f"Elastic Constant for Spring #1 (N/m): {k1:.6f}")
print(f"Elastic Constant for Spring #2 (N/m): {k2:.6f}")

# Output:    
# Elastic Constant for Spring #1 (N/m): 217.179217
# Elastic Constant for Spring #2 (N/m): 234.033196

# Set title
plt.title("Data")

# Set x limits
plt.xlim(0, 5)

# Set x ticks
plt.xticks(np.linspace(0, 5, 5))

# Set x label
plt.xlabel("Mass (kg)")

# Set y ticks
plt.yticks(np.linspace(0, 0.25, 10))

# Set y label
plt.ylabel("Spring elongation (m)")

# Show legend
plt.legend(loc='upper left')

# Text
plt.text(1.25, 0.03, f"Elastic Constant for Spring #1 (N/m): {k1:.6f}", color='b') # Coordinates and text
plt.text(1.25, 0.015, f"Elastic Constant for Spring #2 (N/m): {k2:.6f}", color='r') # Coordinates and text

# Save figure using 300 dots per inch
plt.savefig("lin_regr_scipy.png", dpi=300)

plt.show()
