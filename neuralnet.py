
import numpy as np 
import matplotlib.pyplot as plt


class Sigmoid():
	def __init__(self):
		pass

	def derivative(self, x):
		return self(x) * (1 - self(x))

	def __call__(self, signal):
		signal = np.clip( signal, -500, 500)
		return 1.0/( 1.0 + np.exp( -signal ))

		
def normal_initializer(shape, avg, std):
	return np.random.normal(avg, std, shape)


class Layer():
	def __init__(self, activation):
		self.activation = activation

	def compile(self, input_layer=None):
		pass

	def set_input(self, input):
		self.input = input

	def get_input_(self):
		return self.input

	def get_output(self):
		pass

	def run(self):
		pass

class InputLayer(Layer):
	def __init__(self, nb_neurons, has_bias=True):
		super().__init__(self)
		self.nb_neurons = nb_neurons
		self.has_bias = has_bias
		if has_bias:
			self.nb_neurons += 1

	def compile(self, input_layer=None):
		pass

	def set_input(self, input):
		self.input = input

	def get_output(self):
		return self.input

	def run(self):
		return self.input


class DenseLayer(Layer):
	def __init__(self, nb_neurons, activation, initializer=normal_initializer, has_bias=True):
		super().__init__(activation)
		self.has_bias = has_bias
		self.nb_neurons = nb_neurons
		self.initializer = initializer
		if has_bias:
			self.nb_neurons += 1

	def compile(self, input_layer):
		self.weights = self.initializer((input_layer.nb_neurons, self.nb_neurons), 0.0, 1.0)

	def get_output(self):
		return self.output

	def get_input_(self):
		return np.matmul(self.input, self.weights)


	def run(self):
		self.output = self.activation(self.get_input_())
		#print(self.output)
		return self.output


class FFNNet():
	def __init__(self, input_size, has_bias=True):
		self.layers = [InputLayer(input_size, has_bias)]

	def compile(self):
		assert len(self.layers) > 1
		prev_layer = None
		for layer in self.layers:
			layer.compile(prev_layer)
			prev_layer = layer

	def feedforward(self, input):
		for layer in self.layers:
			layer.set_input(input)
			input = layer.run()
		return input

class Backprop:
	def __init__(self, lr=0.5):
		self.lr = lr

	def calc_delta_step(self, net, y, yo):
		o = len(net.layers)-1
		layer = net.layers[o]
		layer_ = net.layers[o-1]
		delta = np.array(-2 * (y - yo) * (yo * (1-yo)))
		#print(delta.shape)
		o -= 1
		deltas = [delta]
		while o >= 1:
			layer_ = net.layers[o+1]
			delta = np.matmul(layer_.weights, delta.T).T	
			#print(delta.shape)
			deltas.insert(0, delta)
			o -= 1
		return deltas

	def step(self, net, x, y):
		yo = net.feedforward(x)
		delta = self.calc_delta_step(net, y, yo)
		#print(delta[0])
		for l in range(0, len(net.layers)-1):
			layer = net.layers[l]
			layer_ = net.layers[l+1]
			for i in range(layer.nb_neurons):
				for j in range(layer_.nb_neurons):
					layer_.weights[i][j] -= self.lr  * layer.get_output()[i] * delta[l][j]

		error = (y - yo)
		error2 = error**2
		mse = np.sum(error2)/len(x)
		return mse


x = [[1.0, 1.0, 1.0], [1.0, 1.0, 0.001], [1.0, 0.001, 1.0], [1.0, 0.001, 0.001]]
y = [ [0.001, 1.0], [1.0, 0.001], [1.00, 0.001], [0.001, 0.001]]

net = FFNNet(2)
net.layers.append(DenseLayer(5, Sigmoid()))
net.layers.append(DenseLayer(2, Sigmoid(), normal_initializer, False))
net.compile()

optimizer = Backprop(0.9)
EPOCHS = 500
errors = np.zeros(EPOCHS)
for i in range(EPOCHS):
	avg = 0.0
	for j in range(len(x)):
		avg += optimizer.step(net, np.array(x[j]), np.array(y[j]))
	errors[i] = avg/len(x)
plt.plot(errors)
print(net.feedforward(x))
plt.show()





