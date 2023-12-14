import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as gaussian

# Set the random seed for reproducibility
np.random.seed(0)

# Define parameters for the Gaussian mixture
num_samples = 1000
component_means = [(-2, -2), (0, 0), (2, 2)]
component_covs = [np.eye(2), np.eye(2), np.eye(2)]
component_weights = [0.3, 0.4, 0.3]

# Generate random samples from the Gaussian mixture
samples = []
for i in range(num_samples):
    # Choose a component based on the weights
    component = np.random.choice(3, p=component_weights)

    # Generate a sample from the selected component
    sample = np.random.multivariate_normal(component_means[component], component_covs[component])
    samples.append(sample)

samples = np.array(samples)

# Create a 2-D grid for plotting
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
pos = np.dstack((x, y))

# Evaluate the Gaussian mixture PDF at each point in the grid
pdf_values = np.zeros_like(x)
for i in range(len(component_means)):
    pdf_values += component_weights[i] * gaussian.pdf(pos, mean=component_means[i], cov=component_covs[i])

# Create a heatmap plot
plt.figure(figsize=(8, 6))
plt.contourf(x, y, pdf_values, cmap='viridis')
plt.colorbar()
plt.title('2-D Gaussian Mixture')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

