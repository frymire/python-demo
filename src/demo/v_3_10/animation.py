import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

figure, axes = plt.subplots()
line, = axes.plot(x, y)


def init():
    """Initialize the background of the animation."""
    line.set_ydata([np.nan] * len(x))
    return line,


def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,


animation = FuncAnimation(figure, update, frames=100, init_func=init, blit=True)
animation.save('sine_wave_animation.mp4', writer='ffmpeg', fps=30)
plt.close()  # Close the figure to prevent it from displaying in Jupyter notebooks
