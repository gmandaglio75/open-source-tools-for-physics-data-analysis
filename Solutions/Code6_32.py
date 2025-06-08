import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(-10, 0.0001,100)
x2 = np.linspace(0.0001, 10,100)
x =x1 + x2
y1 = np.sin(x1) / x1
y2 = -np.sin(x2) / x2
y=y1+y2
plt.plot(x,y)
plt.show()
