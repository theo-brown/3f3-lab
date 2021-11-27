import numpy as np
import matplotlib.pyplot as plt

plt.figure()

for i, color in enumerate([color1, color2, color3, color4]):
    alpha = i + 1
    plt.hist(nonstandard_samples(10000, alpha), bins=30, color=color, label=r'$alpha = {}$'.format(alpha))

plt.xlabel('x')
plt.ylabel('Number of samples')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))
plt.savefig(f'figures/nonstandard_distribution.png', bbox_inches='tight')