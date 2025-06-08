import numpy as np
import matplotlib.pyplot as plt

# Create a figure of size 8x6 inches, 300 dots per inch
plt.figure(figsize=(8, 6), dpi=300)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 128)
S = np.sin(X)

# Set fonts
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'black','size':15}

# Set title
plt.title("Customize a plot", fontdict = font1, loc = 'right')

# Set x limits
plt.xlim(-4.0, 4.0)

# Set x ticks
plt.xticks(np.linspace(-4, 4, 9))

# Set x label
plt.xlabel("X", fontdict = font2)

# Set y limits
plt.ylim(-1.0, 1.0)

# Set y ticks
plt.yticks(np.linspace(-1, 1, 5))

# Set y label
plt.ylabel("sin(X)", fontdict = font2)

# Plot sine with a red continuous line of width 1 (pixels)
plt.plot(X, S, color="red", linewidth=1.0, linestyle="-", label="sine", marker = 'o')

# Text annotation inside the plot
plt.annotate('min', xy=(-1.6, -1), xytext=(1, -0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

# Show legend
plt.legend(loc='upper left')

# Save figure using 300 dots per inch
plt.savefig("matplotlib_ex2.png", dpi=300)

# Show result on screen
plt.show()

