import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import time

# Clear plots
plt.clf()

# Define symbolic variables
x = sym.symbols('x')
y = sym.symbols('y')

# Initialize parameters
x1 = np.ones(10)
x1[0] = 4.5
x2 = np.ones(10)
x2[0] = 4.5
F = x**3 - 2*x*y**2 + 3*x*y + 2*y**3
F = F.subs(y,14-2*x)
Fprime = sym.diff(F)
FdoublePrime = sym.diff(Fprime)
# Gradient descent with line search
start_time = time.time()
for i in range(9):
    # determine step size using line search
    alpha = 1e-2
    while F.subs(x, x1[i] - alpha*Fprime.subs(x, x1[i])) >= F.subs(x, x1[i]) - 0.5*alpha*(Fprime.subs(x, x1[i])**2):
        alpha *= 0.5 # minimising is performed by dividing half in order to converge faster
    
    # update x1
    x1_new = x1[i] - alpha*Fprime.subs(x, x1[i])
    if abs(((x1_new - x1[i])/x1_new)*100) < 1e-5:
        break
    x1[i+1] = x1_new
    funGD = F.subs(x,x1[i])

end_time_1 = time.time()
# Newton-type
start_time = time.time()
for i in range(9):
    x2_new = x2[i] - (Fprime.subs(x, x2[i])/FdoublePrime.subs(x, x2[i]))
    if abs(((x2_new - x2[i])/x2_new)*100) < 1e-5:
        break
    x2[i+1] = x2_new
    funN = F.subs(x,x2[i])
end_time_2 = time.time()
# Print results
print(f'Due to gradient descent method with line search:\n x1 = {x1[i]:.9f}\n x2 = {14-2*x1[i]:.9f}\n F = {F.subs(x, x1[i]):.9f}\n')
print(f'Gradient descent converged in {i+1} iterations and took {end_time_1 - start_time:.9e} seconds\n')
print(f'Due to Newton\'s type method:\n x1 = {x2[i]:.9f}\n x2 = {14-2*x2[i]:.9f}\n F = {F.subs(x, x2[i]):.9f}\n')
print(f'Newton\'s type converged in {i+1} iterations and took {end_time_2 - start_time:.9e} seconds\n')
# Plot function
xx = np.arange(-50, 60)
X, Y = np.meshgrid(xx, xx)
FF = X**3-2*X*Y**2+3*X*Y+2*Y**3

fig = plt.figure(dpi=1200)
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, FF, cmap='viridis',alpha=0.707)
ax.plot(xx, 14-2*xx, xx**3-2*xx*(14-2*xx)**2+3*xx*(14-2*xx)+2*(14-2*xx)**3, color='m', linewidth=2,label='constraint')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('F')
ax.legend()
# Mark point on plot
ax.scatter(x2[i], 14-2*x2[i], F.subs(x, x2[i]), marker='s', s=10, facecolors='r')
plt.show()

# Results obtained from lagrange multipliers method 
# in order to analyse and compare error percentage of the algorithms
x = [5.036557818,3.92688436]
fun = 152.872609510
# Print the results
print('\nResults obtained from lagrange multipliers method \nin order to analyse and compare error percentage of the algorithms:')
print(f'Real optimal solution:, ({x[0]:.9f},{x[1]:.9f})')
print(f'Real minimum value:, {fun:.9f}\n')

# Error calculations
errGD = ((abs(funGD - fun))/fun)*100
errN = ((abs(funN - fun))/fun)*100

# Print results
print(f'Error percent of Gradient Descent method: {errGD:.9e} %')
print(f'Error percent of Newton\'s type method: {errN:.9e} %\n')
