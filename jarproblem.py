from agent import simple_problem_solver
from agent import Node

class simple_tree_jar_agent:
	def __init__(self):
		self.state = [0,0]
		
	def get_state(self):
		return self.state
		
		
	def update_state(self, percept):
		self.state[0] = percept[0]
		self.state[1] = percept[1]
		return self.state
		
	def formulate_goal(self):
		self.goal = [2, 0]
		return self.goal
		
	def formulate_problem(self):
		self.frontier = []
		pass
	
	def expand(self, node):
		esvaziar_3 = [node.state[0], 0]
		esvaziar_4 = [0, node.state[1]]
		d3_4 = min(node.state[1], max(0,4-node.state[0]))
		d4_3 = min(node.state[0], max(0, 3 - node.state[1]))
		transferir_3_para_4 = [node.state[0] + d3_4, node.state[1] - d3_4]
		transferir_4_para_3 = [node.state[0] - d4_3, node.state[1] + d4_3]
		encher3 = [node.state[0], 3]
		encher4 = [4, node.state[1]]
		return [Node(node, esvaziar_3, 1, "esvaziar 3"), 
				Node(node, esvaziar_4, 1, "esvaziar 4"),
		        Node(node, transferir_3_para_4, 1, "transferir de 3 para 4"),
				Node(node, transferir_4_para_3, 1, "transferir de 4 para 3"),
				Node(node, encher3, 1, "encher 3"),
				Node(node, encher4, 1, "encher 4")]

	def search(self):
		self.frontier.append(Node(None, self.state, 0, "Iniciar"))
		while True:
			if len(self.frontier) == 0:
				return None
			node = self.frontier.pop(0)
			#print(node.state)
			if (node.state[0] == self.goal[0] and node.state[1] == self.goal[1]):
				return node.solution()
			children = self.expand(node)
			for c_node in children:
				self.frontier.append(c_node)
				
def genkey(state):
	return "%d %d"%(state[0], state[1])
				
class simple_graph_jar_agent(simple_tree_jar_agent):
	def __init__(self):
		super().__init__()
		self.closed = {}
		self.frontier_log = {}
	
	def search(self):
		self.frontier.append(Node(None, self.state, 0, "Iniciar"))
		self.frontier_log[genkey(self.state)] = True
		while True:
			if len(self.frontier) == 0:
				return None
			node = self.frontier.pop(0)
			del self.frontier_log[genkey(node.state)]
			if (node.state[0] == self.goal[0] and node.state[1] == self.goal[1]):
				return node.solution()
			self.closed[genkey(node.state)] = True
			children = self.expand(node)
			for c_node in children:
				key = genkey(c_node.state)
				if (not key  in self.closed) and (not key in self.frontier_log): 	
					self.frontier.append(c_node)
					self.frontier_log[key] = True
				
class Environment:
	def __init__(self):
		self.state = [0,0]
	
	def apply_action(self, action):
		print(action)
		d3_4 = min(self.state[1], max(0, 4-self.state[0]))
		d4_3 = min(self.state[0], max(0, 3 - self.state[1]))
		if (action == "encher 3"):
			self.state[1] = 3
		elif (action == "encher 4"):
			self.state[0] = 4
		elif (action == "esvaziar 3"):
			self.state[1] = 0
		elif (action == "esvaziar 4"):
			self.state[0] = 0
		elif (action == "transferir de 3 para 4"):
			self.state = [self.state[0] + d3_4, self.state[1] - d3_4]
		elif (action == "transferir de 4 para 3"):
			self.state = [self.state[0] - d4_3, self.state[1] + d4_3]
			
			
		

if __name__ == "__main__":
	solver = simple_problem_solver(simple_graph_jar_agent())
	env = Environment()
	result = solver.act(env.state)
	env.apply_action(result)
	while env.state[0] != 2 or env.state[1] != 0:
		result = solver.act(env.state)
		env.apply_action(result)
