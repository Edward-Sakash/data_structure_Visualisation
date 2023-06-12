"""# Code challenge for next time.

How to solve an equation numerically in a given interval with a given accuracy.
Let's say we want to find the solution to f(x) = exp(x)+x 
 in the interval [-1,0] within accuracy 0.0001.
  How to do it?"""
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

print("_________________________________________________")

#Solution 2
# the Fixed-Point Iteration method to solve the equation
#  f(x) = exp(x) + x within a given interval and accuracy

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) + x

def fixed_point_iteration(g, x0, accuracy):
    x = x0
    while True:
        x_new = g(x)
        if abs(x_new - x) < accuracy:
            break
        x = x_new
    return x_new

# Define the equation and the iteration function
equation = lambda x: f(x) - x
g = lambda x: -np.log(np.abs(x)) - np.log(1/np.abs(x) + 1) if x < 0 else -np.log(1 + x)

# Set the interval and desired accuracy
a = -1
b = 0
accuracy = 0.0001

# Perform fixed-point iteration to find the solution
solution = fixed_point_iteration(g, (a + b) / 2, accuracy)
print("The solution is:", solution)

# Plot the function and the solution
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y, label='f(x) = exp(x) + x')
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=solution, color='red', linestyle='--', label='Solution')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Plot of f(x) = exp(x) + x')
plt.grid(True)
plt.show()

