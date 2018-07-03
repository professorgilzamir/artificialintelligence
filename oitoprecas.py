from agent import simple_problem_solver
from agent import Node
import numpy as np


class matrix:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.N = self.width * self.height
		self.data = np.random.choice(self.N, self.N, replace=False)

	def get_index(self, i, j):
		return j * self.width + i
	
	def get_coords(self, index):
		i = index//self.width
		return (i, index % self.width)

	def get_zero_coords(self):
		for i in range(0,self.N):
			if (self.data[i] == 0):
				return self.get_coords(i)
		return None

class Environment:
	def __init__(self, N):
		self.state = matrix(N,N)

	def apply_action(self, action):
		#print(action)
		pos = self.state.get_zero_coords()
		idx = self.state.get_index(pos)
		if (action == "SOUTH"):
			if (pos[0] + 1) < self.state.N:
				tmpidx = self.state.get_index(pos[0]+1)
				tmp = self.state.data[tmpidx]
				self.state.data[tmpidx] = self.state.data[idx]
				self.state.data[idx] = tmp
		elif (action == "NORTH"):
			if (pos[0] - 1) > 0:
				tmpidx = self.state.get_index(pos[0]-1)
				tmp = self.state.data[tmpidx]
				self.state.data[tmpidx] = self.state.data[idx]
				self.state.data[idx] = tmp	
		elif (action == "WEST"):
			if (pos[1] - 1) > 0:
				tmpidx = self.state.get_index(pos[1]-1)
				tmp = self.state.data[tmpidx]
				self.state.data[tmpidx] = self.state.data[idx]
				self.state.data[idx] = tmp
		elif (action == "EAST"):
			if (pos[1] + 1) > 0:
				tmpidx = self.state.get_index(pos[1]+1)
				tmp = self.state.data[tmpidx]
				self.state.data[tmpidx] = self.state.data[idx]
				self.state.data[idx] = tmp

class simple_tree_eigth_agent:
	def __init__(self):
		self.state = np.array([7,2,4,5,0,6,8,3,1])
		
	def get_state(self):
		return self.state
		
		
	def update_state(self, percept):
		self.state = percept
		return self.state
		
	def formulate_goal(self):
		self.goal = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
		return self.goal
		
	def formulate_problem(self):
		self.frontier = []
		pass
	
	def expand(self, node):
		pass

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
				
class simple_graph_eigth_agent(simple_tree_jar_agent):
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

if __name__ == "__main__":
	solver = simple_problem_solver(simple_graph_jar_agent())
	env = Environment(3)
	result = solver.act(env.state)
	env.apply_action(result)
	while not np.array_equal(env.state, solver.goal):
		result = solver.act(env.state)
		env.apply_action(result)
	
	#env = matrix(3,3)
	#for i in range(0, env.N):
	#	print("%s : %s"%(env.get_coords(i), env.data[i]))
	#print("--------------------------------------------------------")
	#print(env.get_zero_coords())
