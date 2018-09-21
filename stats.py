from matplotlib import pyplot as plt
import random
import numpy as np

x = np.arange(100) + 1
y = np.zeros(100)

for j in range(1000):
	n = random.randint(1, 100)
	y[n-1] += 1

m = np.mean(y)
std = np.std(y)

plt.plot(x, y, color='r')
plt.plot(x, (y-m)/std)
plt.show()