import csv

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

	def addChild(self, filho, pai):
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

def carregar_dados(path):
	#INICO::ESTA PARTE DO CODIGO REALIZA LEITURA DOS DADOS DO ARQUIVO CSV
	tabela = []
	with open(path, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if (len(row)>3):
				tabela.append([row[0].strip(), row[1].strip(), int(row[2].strip()), int(row[3].strip())])
	return tabela


def arvore_decisao(exemplos, atributos, padrao):
	if (len(exemplos) == 0):
		return padrao

	if len(exemplos) > 0 and mesmaClassificacao(exemplos):
		return No(exemplos[0][0], padrao, None)

	if (len(atributos) == 0):
		return No(maioria(exemplos), padrao, None)

tabela = carregar_dados('teste.txt')
no = arvore_decisao(tabela, [], None)
print(no)
