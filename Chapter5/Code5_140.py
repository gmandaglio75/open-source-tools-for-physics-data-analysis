import matplotlib.pyplot as plt
import numpy as np

# Some data to display
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x ** 2)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Multiple subplots')
ax1.plot(x, y, color='red', marker='o', linestyle='dashed', linewidth=1, markersize=6)
ax2.plot(x, -y, color='orange', marker='o', linestyle='dashed', linewidth=1, markersize=6)
plt.show()
