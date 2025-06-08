import matplotlib.pyplot as plt
import numpy as np

# Generate sample data: velocities of object (in m/s)
np.random.seed(0)
velocities = np.random.normal(loc=50, scale=10, size=1000)  # mean=50, std=10, n=1000

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(velocities, bins=30, color='blue', edgecolor='black')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Frequency')
plt.title('Distribution of Velocities')
plt.grid(True)
plt.savefig("matplotlib_histogram.png", dpi=300)
plt.show()
