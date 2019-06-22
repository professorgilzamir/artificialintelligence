###################################
# Autor: Gilzamir F. Gomes        #
# Copyright (C) Skynet :)~		  #
#								  #
# A existência é apenas um fluxo  # 
#   de sentimentos.				  #
#								  #
###################################

import numpy as np #importa módulo numpy que facilita e agiliza manipulação de matrizes.
import time #importa módulo que permite usar o comando sleep (pausar, a grosso modo), dentre outros.

#Além dos módulos numpy e time, usamos várias construções internas do python, como as funções max e min.
#max e min são operações padrões do python, retornam o maior o menor valor, respectivamente, dentre dois valores dados.
#Listas são estruturas internas do python. Uma lista é uma coleção ordenada de valores delimitada por [ e ] e cujos valores
#são separados por vírgula.
#Dicionários também são estruturas internas e permitem mapear uma chave para um valor. Por exemplo, podemos mapear
#nomes (strings) para idades (inteiros) com a construção:
#>>idade = {'Pedro':50, 'maria':30}
#>>idade['pedro'] # vai retornar o valor 50
#>>idade['maria'] #vai retornar o valor 30
#>>idade['Maria'] #vai gerar um erro to tipo KeyError, pois não existe a chave 'Maria', mas sim 'maria'.
#Portanto, um dicionário é uma lista de pares (Chave, Valor), contudo, delimitada por chaves em vez de colchetes.
#Python também tem suporte a tuplas, que são parecidas com listas, mas são imutáveis. Para diferenciar listas de tuplas,
#em tuplas, usa-se parênteses em vez de colchetes.

ENV_SHAPE = (3, 4) #forma da grade do mundo

env = np.zeros(ENV_SHAPE) #objeto que representa no mundo de grade as posições livres e as paredes.
env[1, 1] = 1
env[1, 2] = 1
env[2, 2] = 1	

rewards = np.zeros(ENV_SHAPE) #Uma matriz com uma célula para cada posição com a recompensa imediata do agente por conseguir estar na posição.
rewards[2,1] = -1.0 #estado no qual o agente morre, posição (2, 1), gera recompensa negativa
rewards[2,3] = 1.0 #estado no qual o agente vence, posição (2, 3), gera recompensa positiva

#posição do agente que representa o estado atual
agent_position = [0, 0]

actions = {'up':0, 'down':1, 'right':2, 'left': 3} #mapeamento de ações para índices.
actions_from_indices = {0:'up', 1:'down', 2:'right', 3:'left'} #mapeamento de índices para ações.

#states_indices faz o mapeamento para estado dado o índice que representa o estado.
states_indices = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3:(0, 3), 4: (1,0), 5: (1, 3), 6: (2, 0), 7: (2, 1), 8: (2, 3)}

#indices_states faz o mapeamento para índice dado o estado correspondente.
indices_states = {(0, 0): 0,(0, 1): 1, (0, 2): 2, (0, 3):3, (1,0):4, (1, 3):5, (2, 0):6, (2, 1):7, (2, 3):8}

#cria a tabela que representa a função Q, com todas as entradas iguais a zero
Q = np.zeros((9, 4)) #Tabela Q

# função reset determina o estado inicial do ambiente
def reset():
	global agent_position
	positions = [[0,0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 0]]
	agent_position = positions[np.random.choice(5)]

#imprime o estado atual do ambiente
def print_world():
	global agent_position, env
	for i in range(3):
		for j in range(4):
			if agent_position[0] == i and agent_position[1] == j:
				print('*', end=' ')
			else:
				print(int(env[i, j]), end=' ')
		print('')

#realiza um passo de simulação dada a ação do agente
def step(action='right'):
	global actions, env, states_indices, indices_states, agent_position
	reward = 0
	action_idx = actions[action]
	prev_pos = agent_position.copy()
	if action_idx == 0:
		agent_position[0] = max(0, agent_position[0]-1)	
	elif action_idx == 1:
		agent_position[0] = min(2, agent_position[0]+1)
	elif action_idx == 2:
		agent_position[1] = min(3, agent_position[1]+1)
	elif action_idx == 3:
		agent_position[1] = max(0, agent_position[1]-1)
	done = False

	tpos = tuple(agent_position)
	if tpos in [(2, 1), (2, 3)]:
		done = True
	elif env[tpos] == 1:
		agent_position[0] = prev_pos[0]
		agent_position[1] = prev_pos[1]

	return agent_position.copy(), rewards[agent_position[0], agent_position[1]], done


#seleciona uma ação com base na tabela Q.
def act():
	global actions, env, states_indices, indices_states, agent_position, actions_from_indices
	state_idx = indices_states[tuple(agent_position)]
	return actions_from_indices[np.argmax(Q[state_idx])]


#implementação do algoritmo q_learning: deve encontrar uma tabela Q que maximiza a recompensa futura esperada.
def q_learning():
	global actions, env, states_indices, indices_states, agent_position
	eps = 1.0
	gamma = 0.9
	eps_decay = 0.999
	global_step = 0
	learning_rate = 1.0
	print(Q[0])
	for i in range(2000):
		done = False
		reset()
		steps = 0
		while not done:
			action = ''
			if np.random.random() <= eps or global_step < 50000:
				action = np.random.choice(['up', 'down', 'right', 'left'])
			else:
				action = act()

			if global_step >= 10000:
				eps = eps * eps_decay
			#print(steps, action, agent_position, eps)
			initial_state = agent_position.copy()
			new_state, reward, done = step(action)
			idx_istate = indices_states[tuple(initial_state)] #DICA: não se pode utilizar uma lista como chave, apenas tuplas, portanto, primeiro tenho que converter a chave de lista para tupla 
			idx_action = actions[action]
			idx_nstate = indices_states[tuple(new_state)]
			Q[idx_istate, idx_action] =  reward + gamma*np.amax(Q[idx_nstate])
			global_step += 1
			steps += 1
			if steps > 10000:
				done = True
		print(i)
		print('LEARNED Q FUNCTION')
		print(Q)


#executa uma simulação depois do agente treinado.
def run():
	global actions, env, states_indices, indices_states, agent_position
	reset()
	#agent_position = [0, 0]
	done = False
	while not done:
		action = act()
		new_state, reward, done = step(action)
		time.sleep(0.5)
		print(action)
		print('--------------------------------------')
		print_world()
		print('--------------------------------------')

q_learning() #treinando o agente
run() #testando o agente
