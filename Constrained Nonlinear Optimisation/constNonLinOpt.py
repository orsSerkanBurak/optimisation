import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def objective(x):
    return -(2*x[0] + x[1] - x[0]**2 - x[1]**2 - 2)

def constraint1(x):
    return  2*x[0] + x[1] - 4

def constraint2(x):
    return  x[0] + 2*x[1] - 4

# Define the range of the variables
xx = np.arange(-5, 5, 0.1)

# Calculate the objective function values
FF = np.zeros((xx.size, xx.size))
for ii in range(xx.size):
    for jj in range(xx.size):
        FF[ii, jj] = -(2*xx[ii] + xx[jj] - xx[ii]**2 - xx[jj]**2 - 2)

# Define the constraints as surfaces
X, Y = np.meshgrid(xx, xx)
g1 = 4 - 2*X - Y  # first constraint
g2 = 4 - X - 2*Y  # second constraint

# Plot the objective function and the constraint surfaces
fig = plt.figure(1,dpi=1200)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, -FF, cmap='viridis', alpha=0.5,label='surface')
ax.plot_surface(X, Y, g1, color='m', alpha=0.3,label='constraint')
ax.plot_surface(X, Y, g2, color='g', alpha=0.3,label='constraint')

# Set labels and view angle
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$F$')
ax.view_init(elev=25, azim=-120)

# Solve the optimization problem
cons = [{'type': 'ineq', 'fun': constraint1}, {'type': 'ineq', 'fun': constraint2}]
res = minimize(objective, [1,1], method='SLSQP', constraints=cons)

# Plot the optimal solution point
ax.plot([res.x[0]], [res.x[1]], [-res.fun], 'rs', markersize=5, markerfacecolor='r')

# Show the plot and print the output
plt.show()
print("Optimal value of the objective function is {:.4f}".format(-res.fun))
print("Optimal point is ({:.4f}, {:.4f})".format(res.x[0], res.x[1]))
