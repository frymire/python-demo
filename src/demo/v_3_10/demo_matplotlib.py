import matplotlib.pyplot as plt
import numpy as np

# Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
x = np.arange(0, 3, 0.1)
x2 = np.square(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, x, label='Identity')
ax.plot(x, x2, label='Squared')

# Add labels and a title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Line Plot')

# Add a legend
ax.legend()

# Show the plot
plt.show()
