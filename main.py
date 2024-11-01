import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the wave equation function
def wave_equation(x, t, x0, num_terms=100):
    pi = np.pi
    y = (2 / (pi**2 * x0 * (1 - x0))) * np.sum([
        (1 / n**2) * np.sin(n * pi * x0) * np.sin(n * pi * x) * np.cos(n * pi * t)
        for n in range(1, num_terms + 1)
    ], axis=0)
    return y

# Set variables
x0 = 0.5  # Middle of the string
num_terms = 100  # Number of terms in the series
x = np.linspace(0, 1, 100)  # Range of x

# Create a figure and axis for the animation
fig, ax = plt.subplots()
line, = ax.plot(x, wave_equation(x, 0, x0, num_terms))
ax.set_title('simulation of wave equation')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylim(-1, 1)
ax.grid()

# Update function for animation
def update(t):
    y = wave_equation(x, t, x0, num_terms)
    line.set_ydata(y)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 200), blit=True)

# Add a __main__ block to run the simulation
if __name__ == "__main__":
    ani.save('wave_equation_x0='+str(x0)+'_num='+str(num_terms)+'.gif', writer='pillow', fps=30)
    plt.show()
