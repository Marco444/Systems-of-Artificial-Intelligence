from layer import Layer
import numpy as np

class MultiLayerPerceptron:
    def __init__(self, perceptrons_for_layers, activation_function):
        """ 
        perceptrons_for_layers: Un arreglo cuyo primer elemento es la cantidad de datos iniciales, y consecuentemente la cantidad de perceptrones por capa
        activation_function: The activation function to execute in the layers
        """

        # Genero los layers
        layers = []
        for index in range(1, len(perceptrons_for_layers)):
            layers.append(Layer(perceptrons_for_layers[index], perceptrons_for_layers[index-1], activation_function))
        
        self.layers = layers
        self.layers_count = len(perceptrons_for_layers)

    def get_all_weights(self):
        return [layer.get_perceptrons_weights_with_bias() for layer in self.layers]

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x


    # x: input de entrada
    # n: tasa de aprendizaje (eta)
    # error: diferencias entre lo esperado y lo calculado para cada neurona de salida
    def backward(self, error, x, n):
        # Obtenemos el theta'(h) de la capa de salida
        activation_diff = self.layers[len(self.layers)-1].get_perceptrons_activation_diff()

        #delta = []
        #for index in range(len(activation_diff)):
        #    delta.append(activation_diff[index]*error[index])
        # Calculamos el d_i para cada neurona de salida
        activation_diff_diagonal = np.diag(activation_diff)
        d = np.matmul(error, activation_diff_diagonal)


        # Obtengo los valores de salida de la anteultima capa
        values = self.layers[len(self.layers)-2].get_perceptrons_activation()

        # n * d_i * V = delta_w
        d_n = n * d

        # Caso particular: Perceptron simple
        if len(self.layers) == 1:
            delta_w = np.matmul(d_n, x)
            return [delta_w]

        # delta_w = np.matmul(np.transpose(d_n), values)

        # TODO: esto esta mal, revisar para el caso de que la ultima sea 1
        final_delta_w = []
        delta_w = np.matmul(np.split(d_n, len(d_n)), np.split(values, 1))
        # print(delta_w)
        final_delta_w.append(delta_w)

        # Obtengo los W antes de actualizar
        #olds_w = self.layers[len(self.layers)-1].get_perceptrons_weights()
        olds_w = self.layers[len(self.layers)-1].get_perceptron_weights_transposed()

        # Ahora hacemos desde mlp el add delta_weights
        #self.layers[len(self.layers)-1].add_perceptrons_delta_weights(delta_w)

        # Itero entre todas las capas
        for index in range(len(self.layers)-2, -1, -1):
            if index != 0:
                values = self.layers[index-1].get_perceptrons_activation()
            else:
                # Si estamos en la capa inferior de la red, utilizamos los datos de entrada
                values = np.insert(x, 0, 1)
            # Calculamos el delta_w y los d_i de los nodos de la capa actual
            delta_w, d = self.layers[index].backward(d, olds_w, n, values)
            # Nos quedamos con una copia de los pesos viejos para la proxima capa
            olds_w = self.layers[index].get_perceptron_weights_transposed()
            final_delta_w.append(delta_w)

            # Ahora hacemos desde mlp el add delta_weights
            # self.layers[len(self.layers)-1].add_perceptrons_delta_weights(delta_w)
            # Actualizamos los pesos de las neuronas de la capa actual
            # self.layers[index].add_perceptrons_delta_weights(delta_w)

        # retorno una lista de matrices con los delta_w en tipo np para la suma
        return final_delta_w


    def apply_delta_w(self, final_delta_w):
        for index, layer in enumerate(self.layers):
            layer.add_perceptrons_delta_weights(final_delta_w[len(self.layers) - index - 1])

        


        
    

    
    


    