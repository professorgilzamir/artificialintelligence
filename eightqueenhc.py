import numpy as np



def inicializar():
	matriz  = np.zeros(8)

	for i in range(8):
		matriz[i] = np.random.choice(8)

	return matriz

def paracima(matriz, i):
	if matriz[i] > 0:
		matriz[i] -= 1
		return True
	return False

def parabaixo(matriz, i):
	if matriz[i] < 7:
		matriz[i] += 1
		return True
	return False

def custo(matriz):
	q = 0
	for i in range(8):
		linha1 = matriz[i]
		for j in range(8):
			if i != j:
				linha2 = matriz[j]
				if (linha1 == linha2 or i == j or abs((linha2-linha1)/(i-j)) == 1.0):
					q += 1
	return q;

def  obter_vizinhos(matriz):
	viz = []
	for i in range(8):
		for j in range(8):
			if i != j:
				v = np.copy(matriz)
				v[i] = j
				viz.append(v)
	return viz



def subida_de_encosta():
	matriz = inicializar()
	while (True):
		custo_atual = custo(matriz)
		vizinhos = obter_vizinhos(matriz)
		vizinhos.sort(key = lambda m: custo(m) )
		if custo(vizinhos[0]) >=  custo_atual:
			return matriz
		else:
			matriz = np.copy(vizinhos[0])


import datetime


matriz = subida_de_encosta()
custo_matriz = custo(matriz)
i = 0
count_suc = 0
count_frac = 0

if custo_matriz > 0:
	count_frac += 1
else:
	count_suc += 1

while i < 10000:
	matriz = subida_de_encosta()
	custo_matriz = custo(matriz)
	if custo_matriz > 0:
		count_frac += 1
	else:
		count_suc += 1
	i += 1
	print(i)
print(count_suc/(count_suc+count_frac))












