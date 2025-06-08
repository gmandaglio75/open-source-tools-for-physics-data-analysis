import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 128)
S = np.sin(X)

# Plot sine
plt.plot(X, S)
# Show result on screen
plt.show()
