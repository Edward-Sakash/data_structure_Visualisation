
###################################################################
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return np.exp(x) + x

# Implement the bisection method
def bisection_method(f, a, b, accuracy):
    if f(a) * f(b) > 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")
    
    while abs(b - a) > accuracy:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

# Define the interval and desired accuracy
a = -1
b = 0
accuracy = 0.0001

# Apply the bisection method to find the solution
solution = bisection_method(f, a, b, accuracy)
print("The solution is:", solution)

# Generate points for the plot
x = np.linspace(a, b, 100)
y = f(x)

# Create the plot
plt.plot(x, y, label='f(x) = exp(x) + x')  # Plot the function
plt.axhline(y=0, color='black', linestyle='--')  # Add a horizontal line at y=0
plt.axvline(x=solution, color='red', linestyle='--', label='Solution')  # Add a vertical line at the solution
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Plot of f(x) = exp(x) + x')
plt.grid(True)
plt.show()
