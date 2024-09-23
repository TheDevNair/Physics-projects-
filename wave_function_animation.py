import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Parameters
L = 1  # Length of the well
hbar = 1  # Reduced Planck's constant (set to 1 for simplicity)
m = 1  # Mass of the particle (set to 1 for simplicity)
n = 1  # Quantum number
frames = 100  # Number of frames in the animation

# Create the figure and axis for the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define spatial and time grids
x = np.linspace(0, L, 100)
t = np.linspace(0, 10, frames)

# Define the wave function
def wave_function(x, t, n):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L) * np.cos(n*2 * np.pi**2 * t / (2 * m * L*2 / hbar))

# Initialize the plot
def init():
    ax.set_xlim(0, L)
    ax.set_ylim(0, max(t))
    ax.set_zlim(-1.5, 1.5)
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Time (t)')
    ax.set_zlabel('Wave Function (ψ(x, t))')
    return fig,

# Update function for animation
def update(frame):
    current_time = t[frame]
    X, T = np.meshgrid(x, t[:frame+1])
    Z = np.array([[wave_function(xi, ti, n) for xi in x] for ti in t[:frame+1]])
    ax.plot_surface(X, T, Z, cmap='viridis', edgecolor='none')
    ax.set_xlim(0, L)
    ax.set_ylim(0, max(t))
    ax.set_zlim(-1.5, 1.5)
    ax.set_xlabel('Position (x)')
    ax.set_ylabel('Time (t)')
    ax.set_zlabel('Wave Function (ψ(x, t))')
    return fig,

# Create animation
anim = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=50)

# Display the animation
plt.show()

# Optionally save the animation to a file (e.g., as an MP4)
# anim.save('wave_function_animation.mp4', writer='ffmpeg', fps=20)
