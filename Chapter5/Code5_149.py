from scipy.integrate import quad

# Define a simple function for integration
def integrand(x):
    return x**3

# Perform numerical integration
result, error = quad(integrand, 0, 1)
print(f"Integral result: {result}, Error estimate: {error}")

# Output: Integral result: 0.25, Error estimate: 2.7755575615628914e-15
