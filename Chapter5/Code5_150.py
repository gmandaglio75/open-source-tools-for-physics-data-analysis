import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Given data points
x = np.arange(0, 10)
y = np.exp(-x / 3.0)

# Create an interpolation function
f = interpolate.interp1d(x, y)

# New x values for interpolation
xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)  # Interpolated y values

# Plotting the results
plt.plot(x, y, 'o', label='data points')
plt.plot(xnew, ynew, '-', label='interpolated curve')
plt.legend()
plt.show()
