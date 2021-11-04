import numpy as np
import matplotlib.pyplot as plt


def ksdensity(x_values, samples, width=0.3):
    def gaussian_pdf(x, mu=0, sigma=1):
        u = (x - mu) / abs(sigma)
        y = (1 / (np.sqrt(2 * np.pi) * abs(sigma)))
        return y * np.exp(-0.5 * u**2)
    # Generate an array of kernel values centred on the samples
    kernel_values = [gaussian_pdf(x_value, samples, width) for x_value in x_values]
    return np.average(kernel_values, axis=1)

# Plot normal distribution
fig, ax = plt.subplots(2)
X = np.random.randn(1000)
ax[0].hist(X, bins=30)
x_values = np.linspace(-5, 5, 100)
ax[1].plot(x_values, ksdensity(x_values, X, width=0.4))
plt.show()