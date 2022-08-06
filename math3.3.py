import numpy as np

import matplotlib.pyplot as plt

x = []
x2 = []
y = []
y2 = []

for i in range(1500):
    r = 1000
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='r')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y, color='r')
plt.axis('scaled')
plt.show()

x = []
x2 = []
y = []
y2 = []

for i in range(1000):
    a = 40
    b = 20
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y, color='r')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y, color='r')
plt.axis('scaled')
plt.show()

x = []
x2 = []
y = []
y2 = []

for i in range(1000):
    a = 400
    b = 200
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y, color='r')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y, color='r')
plt.axis('scaled')
plt.show()