from matplotlib import pyplot as plt
import random
import numpy as np

N = 1000

amostras = []
for i in range(N):
	amostras.append(np.random.randint(1, 101, 100))

medias = []
for i in range(N):
	medias.append(np.mean(amostras[i]))

hist = np.zeros(100)

for i in range(N):
	idx = int(medias[i])
	hist[idx-1] += 1

plt.bar(np.arange(1,101), hist)
plt.show()
