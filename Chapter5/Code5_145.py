import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for two different sets of velocities
np.random.seed(0)
velocities1 = np.random.normal(loc=50, scale=10, size=1000)  # mean=50, std=10, n=1000
velocities2 = np.random.normal(loc=60, scale=15, size=1000)  # mean=60, std=15, n=1000

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12), sharex=True)

# First histogram
axs[0].hist(velocities1, bins=30, color='blue', edgecolor='black', label='Set 1')
axs[0].set_ylabel('Frequency')
axs[0].legend()
axs[0].grid(True)

# Second histogram
axs[1].hist(velocities2, bins=30, color='green', edgecolor='black', label='Set 2')
axs[1].set_xlabel('Velocity (m/s)')
axs[1].set_ylabel('Frequency')
axs[1].legend()
axs[1].grid(True)

# Add a single title for the entire figure
fig.suptitle('Comparison of Velocities', fontsize=16)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("matplotlib_histograms-comp.png", dpi=300)
plt.show()
