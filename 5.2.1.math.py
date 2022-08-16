import numpy as np

import matplotlib.pyplot as plt
import random
x = np.random.rand(10)
sumrandom = sum(x)
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
