import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as gaussian


class GMM:
    """Gaussian Mixture Model """

    np.random.seed(0)  # Set the random seed for reproducibility

    def __init__(self, components):
        self.components = components
        self.num_components = len(self.components)

    def pdf(self, x):
        return sum(c.weight * gaussian.z(x, mean=c.mean, cov=c.covariance) for c in self.components)

    def sample(self, num_samples=None):
        if num_samples is None:
            c = np.random.choice(3, p=[c.weight for c in self.components])
            return self.components[c].sample()
        else:
            return [self.sample() for _ in range(num_samples)]

    def compute_heatmap(self, x, y):
        pdf = np.zeros_like(x)
        xy = np.dstack((x, y))
        for c in self.components:
            pdf += c.weight * gaussian.pdf(xy, mean=c.mean, cov=c.covariance)
        return pdf


class GaussianComponent:
    """Gaussian Component"""

    def __init__(self, weight, mean, covariance):
        self.weight = weight
        self.mean = np.array(mean)
        self.covariance = np.array(covariance)
        self.dimension = len(mean)
        if self.covariance.shape != (self.dimension, self.dimension):
            raise ValueError(
                f"Dimensions of covariance do not match self.dimension. Expected ("
                f"{self.dimension}, "
                f"{self.dimension}), "
                f"but got {self.covariance.shape}")

    def likelihood(self, x):
        return gaussian.z(x, mean=self.mean, cov=self.covariance)

    def sample(self):
        return np.random.multivariate_normal(self.mean, self.covariance)

# Test code...
if __name__ == "__main__":

    c1 = GaussianComponent(0.3, (1, 1), np.diag([0.25, 3]))
    c2 = GaussianComponent(0.2, (3, 4), np.eye(2))
    c3 = GaussianComponent(0.5, (5, 5), np.array([[2, -1.2], [-1.2, 2]]))
    gmm = GMM([c1, c2, c3])

    plt.figure(figsize=(12, 9))

    (x_min, x_max, x_grid) = (-2, 10, 100)
    (y_min, y_max, y_grid) = (-2, 10, 100)
    x, y = np.meshgrid(np.linspace(x_min, x_max, x_grid), np.linspace(y_min, y_max, y_grid))
    z = gmm.compute_heatmap(x, y)

    plt.title('2-D Gaussian Mixture')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.contourf(x, y, z, cmap='viridis')
    plt.colorbar()

    samples = np.array(gmm.sample(1000))
    plt.scatter(samples[:, 0], samples[:, 1], s=10, alpha=0.6, color='red')
    plt.show()
