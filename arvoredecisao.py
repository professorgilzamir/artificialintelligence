import numpy as np
from matplotlib import pyplot
import csv


def log2(x):
	if x:
		return np.log(x)/np.log(2)
	else:
		return 0.0

def entropia2(p, n):
	pa = p/(p+n)
	pb = n/(p+n)
	return - pa * log2(pa) - pb * log2(pb)


def entropia(exemplos, a, b):
	na = 0
	nb = 0
	for e in exemplos:
		if e == a:
			na += 1
		elif e == b:
			nb += 1

	pa = na/len(exemplos)
	pb = nb/len(exemplos)

	return - pa * log2(pa) - pb * log2(pb)


class No:
	def __init__(self, rotulo="", pai=None, filhos=[]):
		self.rotulo = rotulo
		self.pai = pai
		if (filhos):
			self.filhos = filhos.copy()
		else:
			self.filhos = None

	def __str__(self):
		return "(Rotulo: %s, Pai: %s, Filhos: %s)"%(self.rotulo, self.pai, self.filhos)

class Arvore:
	def __init__(self, raiz):
		self.raiz = raiz;

	def adicionarFilho(self, filho, pai):
		pai.filhos.append(filho)

def mesmaClassificacao(exemplos):
	l = exemplos[0][0]
	for e in exemplos:
		if not (e[0] == l):
			return False
	return True 

def maioria(exemplos):
	dics = {}
	for e in exemplos:
		dics[e[0]] = 0

	for e in exemplos:
		dics[e[0]] += 1

	max_v = -1
	max_k = None
	for k in dics.keys():
		if dics[k] > max_v:
			max_v = dics[k]
			max_k = k
	return max_k

def filtrar_exemplos(exemplos, rotulo):
	pass

def filtrar_atributos(atributos, rotulos):
	pass

def carregar_dados(path):
	#INICO::ESTA PARTE DO CODIGO REALIZA LEITURA DOS DADOS DO ARQUIVO CSV
	tabela = []
	with open(path, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if (len(row)>3):
				tabela.append([row[0].strip(), row[1].strip(), int(row[2].strip()), int(row[3].strip())])
	return tabela

def escolherMelhorAtributo(exemplos, atributos):
	return random.choice(atributos)


def arvore_decisao(exemplos, atributos, valores, padrao):
	if (len(exemplos) == 0):
		return padrao

	if len(exemplos) > 0 and mesmaClassificacao(exemplos):
		return No(exemplos[0][0], padrao, None)

	if (len(atributos) == 0):
		return No(maioria(exemplos), padrao, None)

	melhor = escolherMelhorAtributo(exemplos, atributos)
	arvore = No(melhor.rotulo, None, [])
	for v in valores[no.rotulo]:
		exemplos = filtrar_exemplos(exemplo, no.rotulo)
		atributos = filhar_atributos(atributos, no.rotulo)
		subarvore = arvore_decisao(exemplos, atributos, valores, no)
		arvore.filhos.append(subarvore)
	return arvore

tabela = carregar_dados('teste.txt')
no = arvore_decisao(tabela, [], None)
print(escolherMelhorAtributo(None, [1, 2, 3]))
