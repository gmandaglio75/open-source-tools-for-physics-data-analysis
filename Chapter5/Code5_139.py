import matplotlib.pyplot as plt
import numpy as np

# Some data to display
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x ** 2)

fig, ax = plt.subplots()
ax.plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=1, markersize=6)
ax.set_title('Single subplot()')
plt.show()
