from numpy import exp, dot, array, random


class NeuralKahn:
    def __init__(self):
        random.seed(1)

        self.synapsis_weight = 2 * random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def sig_der(self ,x):
        return x * (1 - x)

    def train(self, inputs, outputs, iterations):
        for i in range(iterations):
            output = self.think(inputs)
            error = outputs - output
            adj = dot(inputs.T, error * self.sig_der(output))

            self.synapsis_weight += adj

    def think(self, input):
        return self.sigmoid(dot(input, self.synapsis_weight))

if __name__ == '__main__':
    neuron = NeuralKahn()

    print('Веса до тренировки.')
    print(neuron.synapsis_weight, end='\n\n')

    example_input = array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])

    example_output = array([
    [0,
     1,
     1,
     0]
]).T

    neuron.train(example_input, example_output, 1000000)

    print('Веса после тренировки.')
    print(neuron.synapsis_weight, end='\n\n')

    print('Новая ситуация [1, 0, 0] ->.')
    print(neuron.think(array([[1, 0, 0]])))
