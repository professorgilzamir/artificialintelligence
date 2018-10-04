import numpy as np
import csv
from matplotlib import pyplot as plt

#Função aproximadora
def f(X, W):
	return 1.0/(1.0+np.exp(-1 * np.dot(X,W)))

#cacula a perda durante treinamento
def loss(X, W, Y):
	return np.sum((Y - f(X, W))**2)/len(X)

#calcula o gradiente
def grad(X, Y, W):
	fxw = f(X, W)
	return -2 * (Y-fxw) * fxw * (1.0-fxw) * W

def carregar_dados(path):
	#INICO::ESTA PARTE DO CODIGO REALIZA LEITURA DOS DADOS DO ARQUIVO CSV
	x = []
	y = []
	with open(path, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if (len(row)>3):
				x.append([float(row[0].strip()), 
					float(row[1].strip()), float(row[2].strip()), float(row[3].strip()), 
					float(row[4].strip()), float(row[5].strip()), float(row[6].strip()), 
					float(row[7].strip()), 1.0])
				y.append(float(row[8].strip()))
	return (np.array(x), np.array(y))

(x, y) = carregar_dados("pimaindia.txt")
w =  np.random.normal(0, 0.1, 9) # cada peso é inicializado com uma distribuição normal de média 0 e desvio padrao de 0.1
error = 0.0
lr = 0.1

#INICIO: NORMALIZA OS DADOS - NORMALIZACAO Z
media = np.zeros(8)
for i in range(len(x)):
	for j in range(8):
		media[j] += x[i][j]
media = media/len(x)


desvio = np.zeros(8)
for i in range(len(x)):
	for j in range(8):
		desvio[j] = (x[i][j]-media[j])**2
desvio = np.sqrt(desvio/(len(x)-1))

for i in range(len(x)):
	for j in range(8):
		x[i][j] = (x[i][j]-media[j])/desvio[j]
#FIM:NORMALIZA OS DADOS

MAX_STEPS = 1000
xa = np.arange(MAX_STEPS)
ya = np.zeros(MAX_STEPS)

for i in range(MAX_STEPS):
	xi = np.random.randint(len(x))
	g = grad(x[xi], y[xi], w)
	w -= lr * g
	error = loss(x, w, y)
	print(error)
	ya[i] = error

plt.plot(xa, ya)
plt.xlabel('Época')
plt.ylabel('Erro quadrático médio')
plt.show()




