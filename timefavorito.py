import matplotlib.pyplot as plt
import numpy as np
import csv

'''
Este programa utiliza tabela verdade para tentar advinhar
qual time o usuário torce dentre todos os times cadastrados
no dataset timefavorito.txt.
'''


#INICO::ESTA PARTE DO CODIGO REALIZA LEITURA DOS DADOS DO ARQUIVO CSV
tabela = {}
with open('timefavorito.txt', 'r') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		if (len(row)>3):
			tabela[row[0].strip()] = [row[1].strip(), int(row[2]), int(row[3])]
#FIM::

'''
Esta funcao gera um dicionario que associa estados a times de futebol
retornando um dicionario cuja chave eh a sigla do estado e o valor eh uma
lista de nomes de times de futebol deste estado.
Parametros:

tabela: dicionario indexado por nome do time de futebol. Cada
chave eh associada a uma lista contendo os atributos desse time
na seguinte ordem: estado (sigla), quantidade de campeonatos brasileiros vencidos e
quantidade de copas do brasil vencidas. 

exemplos_atuais: lista dos nomes dos times a serem considerados nessa separacao.
'''
def sep_estado(tabela, exemplos_atuais):
	exemplos = {}
	for nome in exemplos_atuais:
		valor = tabela[nome][0]
		if (valor in exemplos):
			exemplos[valor].append(nome)
		else:
			exemplos[valor] = [nome]
	return exemplos

'''
Retorna um código de acordo com o valor da variável 'valor'.
Se valor for zero, retorna 0.
Se valor for menor do que 3 e maior do que zero, retorna 1.
Se valor for menor do que 4 e maior ou igual a 3, return 2.
Se valor for maior do que 5, retorna 3.
'''
def codigo_titulos(valor):
	if valor < 1:
		return 0
	elif valor < 3:
		return 1
	elif valor < 5:
		return 2
	else:
		return 3


'''
Esta funcao gera um dicionario que associa quantidade de títulos
de determinado campeonato (campeonato=1 significa brasileirao,
 campeaonato=2 significa copa do brasil) a times de futebol
retornando um dicionario cuja chave eh o código que
representa um intervalo de campeonatos vencidos
 e o valor eh uma lista de nomes de times de futebol que venceu
 uma quantidade de campeonatos nesse intervalo.
	Por exemplo,
	tabela = {'Flagmento':['RJ', 5, 3], 'Sao Paulo':['SP': 6, 0], 'Ceara': ['CE', 0, 0]}
	sep_titulos(tabela, tabela.keys(), campeonato=1) retorna um dicionário:
	{0:'CE', 2:['Flamento'], '3':['Sao Paulo']}
	pois 
	0 é o código para times que não venceram nenhum campeonato,
	2 é o código para times que venceram menos de 5 campeonatos e
	3 é o código para times que venceram mais de 5 campeonatos.

Parametros:

tabela: dicionario indexado por nome do time de futebol. Cada
chave eh associada a uma lista contendo os atributos desse time
na seguinte ordem: estado (sigla), quantidade de campeonatos brasileiros vencidos e
quantidade de copas do brasil vencidas. 

exemplos_atuais: lista dos nomes dos times a serem considerados nessa separacao.
'''
def sep_titulos(tabela, exemplos_atuais, campeonato=1):
	exemplos = {}
	for nome in exemplos_atuais:
		valor = codigo_titulos(int(tabela[nome][campeonato]))
		if (valor in exemplos):
			exemplos[valor].append(nome)
		else:
			exemplos[valor] = [nome]
	return exemplos


if __name__=="__main__":
	print("Qual o estado do seu time(Digite a sigla - CE, SP, RJ ou MG)")
	UF = input()
	subestados = sep_estado(tabela, tabela.keys())

	if len(subestados[UF]) == 1:
		print("Você é um torcedor fanático do %s"%(subestados[UF][0]))
	else:
		print("Quantos brasileirões seu time conquistou?")
		n1 = codigo_titulos(int(input()))
		subestados = sep_titulos(tabela, subestados[UF])
		if len(subestados[n1]) == 1:
			print("Você é um torcedor fanático do %s"%(subestados[n1][0]))
		else:
			print("Quantas copas do brasil seu time conquistou?")
			n2 = codigo_titulos(int(input()))
			subestados = sep_titulos(tabela, subestados[n1], campeonato=2)
			if len(subestados[n2]) == 1:
				print("Você é um torcedor fanático do %s"%(subestados[n2][0]))
			else:
				print("Você torce para um dos seguintes times:%s"%(subestados[n2]))




