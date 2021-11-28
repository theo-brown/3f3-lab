# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm
#
# N = 100
# x = np.random.normal(10000)
# nbins = 30
# color1 = 'steelblue'
# color2 = 'firebrick'
#
#
# bin_counts, bin_edges = plt.hist(x[:N], bins=nbins,
#                                  color=color1, label=f'Histogram of {N} samples ({nbins} bins)')
# bin_centres =
# bin_probability = norm.cdf(bin_edges[:-1]) - norm.cdf(bin_edges[1:])
#
# plt.xlabel('x')
# plt.ylabel('Number of samples')
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))
# plt.savefig(f'figures/uniform_histogram_{N}.png', bbox_inches='tight')
import numpy as np               # Only used to generate the data
import matplotlib.pyplot as plt

x = np.random.randn(1000)

plt.figure()

# Matplotlib's pyplot.hist returns the bin counts, bin edges,
# and the actual rendered blocks of the histogram (which we don't need)
bin_counts, bin_edges, patches = plt.hist(x, bins=30)
bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2

# Generate some dummy error values, of the same dimensions as the bin counts
y_error = np.random.rand(bin_counts.size)*10

# Plot the error bars, centred on (bin_centre, bin_count), with length y_error
plt.errorbar(x=bin_centres, y=bin_counts, yerr=y_error, fmt='o', capsize=2)

plt.show()