from agent import simple_problem_solver
from agent import Node
import random as rd
import bisect

def count_inversions(state):
	c = 0
	for i in range(len(state.data)-1):
		if state.data[i] < state.data[i+1] and  not (state.data[i] == 0 and state.data[i+1]==0):
			c += 1
	return c

def calc_parity(state):
	return count_inversions(state) + state.get_zero_coords()[0]
	

def print_state(state):
	for i in range(state.width):
		for j in range(state.height):
			print("%d "%(state.get(i, j)), end="")
		print()

def h(agent, n):
	#implemente sua heuristica aqui
	return 0

def f(agent, n):
	return n.path_cost + h(agent, n)

class ComparableNode(Node):
	def __init__(self,parent, state, step_cost, action, fcost=0):
		super().__init__(parent, state, step_cost, action)
		self.fcost = fcost
		self.fcost = fcost

	def __lt__(self, other):
		if (other):
			return self.fcost < other.fcost
		return false

	def __le__(self, other):
		if (other):
			return self.fcost <= other.fcost
		return False

	def __gt__(self, other):
		if (other):
			return self.fcost > other.fcost
		return False

	def __ge__(self, other):
		if (other):
			return self.fcost > other.fcost
		return false
		
class matrix:
	def __init__(self, nlines, ncolumns, data=None):
		self.width = ncolumns
		self.height = nlines
		self.N = self.width * self.height
		if (data):
			self.data = data
		else:
			values = []
			for i in range(self.N):
				values.append(0) 
			self.data = rd.sample(values, self.N)
	
	def get_index(self, line, column):
		return  line * self.width + column
	
	def get_coords(self, index):
		line = index//self.width
		return (line, index % self.width)

	def get_zero_coords(self):
		for i in range(0,self.N):
			if (self.data[i] == 0):
				return self.get_coords(i)
		return None
		
	def get(self, i, j):
		return self.data[self.get_index(i, j)]
	
	def set(self, i, j, v):
		idx = self.get_index(i, j)
		self.data[idx] = v
	
	def get_position(self, value):
		for i in range(self.N):
			if (value == self.data[i]):
				return self.get_coords(i)
		return None
		
	def copy(self):
		return matrix(self.width, self.height, self.data.copy())

class Environment:
	def __init__(self, N):
		self.state = matrix(N,N)
		self.N = N

	def apply_action(self, action, state=None):
		#print(action)
		if (state == None):
			state = self.state
		pos = state.get_zero_coords()
		idx = state.get_index(pos[0], pos[1])
		if (action == "SOUTH"):
			if (pos[1] + 1) < self.N:
				tmpidx = state.get_index(pos[0], pos[1]+1)
				tmp = state.data[tmpidx]
				state.data[tmpidx] = state.data[idx]
				state.data[idx] = tmp
		elif (action == "NORTH"):
			if (pos[1] - 1) >= 0:
				tmpidx = state.get_index(pos[0], pos[1]-1)
				tmp = state.data[tmpidx]
				state.data[tmpidx] = state.data[idx]
				state.data[idx] = tmp	
		elif (action == "WEST"):
			if (pos[0] - 1) >= 0:
				tmpidx = state.get_index(pos[0]-1, pos[1])
				tmp = state.data[tmpidx]
				state.data[tmpidx] = state.data[idx]
				state.data[idx] = tmp
		elif (action == "EAST"):
			if (pos[0] + 1) < self.N:
				tmpidx = state.get_index(pos[0]+1, pos[1])
				tmp = state.data[tmpidx]
				state.data[tmpidx] = state.data[idx]
				state.data[idx] = tmp
		return state

class simple_tree_eight_agent:
	def __init__(self, environment=None, N=3, initial_state=[7,2,4,5,0,6,8,3,1]):
		self.state = matrix(N, N)
		self.state.data = initial_state.copy()
		self.N = N
		self.environment = environment
		self.initial_state = initial_state
		
	def get_state(self):
		return self.state
		
		
	def update_state(self, percept):
		self.state = percept
		return self.state
		
	def formulate_goal(self, goal_value=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
		self.goal = matrix(self.N, self.N)
		self.goal.data = goal_value
		return self.goal.copy()
		
	def formulate_problem(self):
		self.state.data = self.initial_state.copy()
		self.actions = []
		self.frontier = []
	
	def objective_test(self, state):
		if 	(state.data == self.goal.data):
			#print(state.data)
			#print(self.goal.data)
			return True
		else:
			return False
		
	def expand(self, node):
		south_state = self.environment.apply_action("SOUTH", node.state.copy())
		north_state = self.environment.apply_action("NORTH", node.state.copy())
		west_state = self.environment.apply_action("WEST", node.state.copy())
		east_state = self.environment.apply_action("EAST", node.state.copy())
		
		return [ ComparableNode(node, south_state, 1, "SOUTH"), ComparableNode(node, north_state, 1, "NORTH"),
					ComparableNode(node, west_state, 1, "WEST"), ComparableNode(node, east_state, 1, "EAST") ]

	def search(self):
		self.frontier.append(Node(None, self.state.copy(), 1, None))
		while True:
			if len(self.frontier) == 0:
				return None
			node = self.frontier.pop(0)
			if (self.objective_test(node.state)):
				print(node.state)
				return node.solution()
			children = self.expand(node)
			for c_node in children:
				self.frontier.append(c_node)
				
def genkey(state):
	return "%d %d %d %d %d %d %d %d %d"%(state.data[0], state.data[1], state.data[2], state.data[3], state.data[4], state.data[5], state.data[6], state.data[7], state.data[8])
				
class simple_graph_eight_agent(simple_tree_eight_agent):
	def __init__(self,  environment=None, N=3, initial_state=[7,2,4,5,0,6,8,3,1]):
		super().__init__(environment, N, initial_state)
	
	def search(self):
		self.closed = {}
		self.frontier_log = {}
		self.frontier.append(Node(None, self.state, 0, None))
		self.frontier_log[genkey(self.state)] = True
		while True:
			if len(self.frontier) == 0:
				return None
			node = self.frontier.pop(0)
			del self.frontier_log[genkey(node.state)]
			if (self.objective_test(node.state)):
				return node.solution()
			self.closed[genkey(node.state)] = True
			children = self.expand(node)
			for c_node in children:
				key = genkey(c_node.state)
				if (not key  in self.closed) and (not key in self.frontier_log): 	
					self.frontier.append(c_node)
					self.frontier_log[key] = True


class astar_agent(simple_tree_eight_agent):
	def __init__(self,  environment=None, N=3, initial_state=[7,2,4,5,0,6,8,3,1]):
		super().__init__(environment, N, initial_state)

	def search(self):
		self.closed = {}
		self.frontier_log = {}
		self.frontier.append(Node(None, self.state, 0, None))
		self.frontier_log[genkey(self.state)] = True
		while True:
			if len(self.frontier) == 0:
				return None
			node = self.frontier.pop(0)
			
			del self.frontier_log[genkey(node.state)]
			if (self.objective_test(node.state)):
				print("SOLUTION")
				print_state(node.state)
				return node.solution()
			self.closed[genkey(node.state)] = True
			children = self.expand(node)
			for c_node in children:
				key = genkey(c_node.state)
				if (not key  in self.closed) and (not key in self.frontier_log): 	
					c_node.fcost = f(self, c_node)
					bisect.insort_right(self.frontier, c_node)
					self.frontier_log[key] = True	
					
if __name__ == "__main__":
	env = Environment(3)
	agent = astar_agent(env)
	solver = simple_problem_solver(agent)
	env.state = agent.state.copy()
	action = solver.act(env.state)
	print("START")
	print_state(env.state)
	env.apply_action(action)
	print("%s"%(action))
	print_state(env.state)
	while not (agent.objective_test(env.state)):
		action = solver.act(env.state)
		env.apply_action(action)
		print("%s"%(action))
		print_state(env.state)
	'''
	agent.state.data = [7, 6, 3, 2, 5, 1, 0, 8, 4]
	print("Initial State: ")
	print_state(agent.state)
	initial = Node(None, agent.state, 1, None)
	
	succ = agent.expand(initial, env)
	print("----------------------------------------------")
	print("Sucessores")
	for s in succ:
		if (s.state):
			print("------------------------------------") 
			print_state(s.state)
	print('==============================================================================')
	'''
	'''
	env = matrix(3,3)
	for i in range(0, env.N):
		c = env.get_coords(i)
		print("%s : %d : %s"%(c, env.get_index(c[0], c[1]), env.data[i]))
	print("--------------------------------------------------------")
	for i in range(3):
		for j in range(3):
			print(env.get(i, j))
	'''