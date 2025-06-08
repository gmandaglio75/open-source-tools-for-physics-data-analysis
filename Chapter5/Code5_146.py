import matplotlib.pyplot as plt
import numpy as np

# Data
acceleration = np.array([1, 2, 3, 4, 5])  # acceleration values
force = np.array([11, 19, 31, 40, 52])  # force measurements

# Example variable error bar values
force_err = np.array([1, 2, 1.5, 3, 2.5])  # uncertainties in force measurements
acceleration_err = np.array([0.1, 0.2, 0.15, 0.3, 0.25])  # uncertainties in acceleration measurements

plt.figure()
plt.errorbar(acceleration, force, xerr=acceleration_err, yerr=force_err, fmt='o')
plt.xlabel(r'Acceleration (m/s$^2$)')
plt.ylabel('Force (N)')
plt.title('Force Measurements with Error Bars')
plt.savefig("matplotlib_errors-bar.png", dpi=300)
plt.show()
