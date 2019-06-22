
import numpy as np


'''
Constroi o no que representa o estado inicial. 
O estado inicial eh o trivial com um container para cada objeto.
'''
def make_node(M, bins):
	s = np.zeros((M, M)) #cria matriz M por M.
	for idx, b in enumerate(bins): 
		s[0, idx] = b #coloca em cada recipiente um objeto
	return s


'''
Retorna a última posicao nao vazia de um dado container
'''
def last_noempty_position(state, container): 
	result = np.where(state[:, container] != 0)
	if len(result) > 0 and len(result[0]) > 0:
		return result[0][-1]
	return -1

'''
Retorna a primeira posicao vazia de um dado container
'''
def first_empty_position(state, container):
	result = np.where(state[:, container] == 0)
	if len(result) > 0 and len(result[0])>0:
		return result[0][0]
	return -1

'''
Transfere o conteudo de um container x para um container y
'''
def transfer(x, y, state, max_value=50):
	p = last_noempty_position(state, x)
	if p < 0: #o primeiro container esta vazio
		return False #nao foi possivel transferir
	q = first_empty_position(state, y) 

	if q < 0: #o segundo container esta cheio
		return False #nao foi possivel transferir
	if np.sum(state[:, y]) + state[p, x] <= max_value:
		state[q, y] = state[p, x]
		state[p, x] = 0
		return True
	else:
		return False


def value(state, M):
	count = 0
	for c in range(M):
		if last_noempty_position(state, c)>=0:
			count += 1
	return count

def successors(state, M, N=50):
	suc = []
	columns = []

	for i in range(M):
		if last_noempty_position(state, i) >= 0:
			columns.append(i)

	for c1 in columns:
		for c2 in columns:
			if c1 != c2:
				nstate = np.copy(state)
				transfer(c1, c2, nstate, N)
				suc.append(nstate)
	return suc


def hillclibing(M, N, itens, max_steps=100):
	current_state = make_node(M, itens)
	count = 0
	while True:
		current_value = value(current_state, M)
		if count >= max_steps:
			print("stoped....")
			print(current_state)
			print(current_value)
			break;
		suc = successors(current_state, M, N)
		idx = -1
		min_value = 1000000000000000000
		for i, s in enumerate(suc):
			s_value = value(s, M)
			if s_value < min_value:
				idx = i
				min_value = s_value
		if min_value >= current_value:
			print(current_state)
			print(current_value)
			break
		if idx != -1:
			current_state = suc[idx]
			current_value = min_value
		count += 1

file = open("Falkenauer_t120_00.txt", 'r')

M = int(file.readline())
N = int(file.readline())
itens = []
for line in file:
	itens.append(int(line))
print(len(itens))
hillclibing(M, N, itens, 10)
