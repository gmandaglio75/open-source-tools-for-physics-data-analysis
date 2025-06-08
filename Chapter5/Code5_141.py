import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read a .csv file
data = pd.read_csv('...\hooke.csv')
data
# Output:  Index   "Mass (kg)"   "Spring 1 (m)"   "Spring 2 (m)"
#       0      1          0.00            0.050            0.050
#       1      2          0.49            0.066            0.066
#       2      3          0.98            0.087            0.080
#       3      4          1.47            0.116            0.108
#       4      5          1.96            0.142            0.138
#       5      6          2.45            0.166            0.158
#       6      7          2.94            0.193            0.174
#       7      8          3.43            0.204            0.192
#       8      9          3.92            0.226            0.205
#       9     10          4.41            0.238            0.232

# Plot data in the same graph
ax1 = plt.scatter(x = data[' "Mass (kg)"'], y=data[' "Spring 1 (m)"'], label='Spring 1')
ax2 = plt.scatter(x = data[' "Mass (kg)"'], y=data[' "Spring 2 (m)"'], label='Spring 2')

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

# Save figure using 300 dots per inch
plt.savefig("pandas_matplotlib.png", dpi=300)

plt.show()
