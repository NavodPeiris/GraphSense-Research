
import numpy as np


class TwoHiddenLayerNeuralNetwork:
    def __init__(self, input_array: np.ndarray, output_array: np.ndarray) -> None:

        
        self.input_array = input_array

        
        
        

        
        
        
        rng = np.random.default_rng()
        self.input_layer_and_first_hidden_layer_weights = rng.random(
            (self.input_array.shape[1], 4)
        )

        
        
        
        self.first_hidden_layer_and_second_hidden_layer_weights = rng.random((4, 3))

        
        
        
        self.second_hidden_layer_and_output_layer_weights = rng.random((3, 1))

        
        self.output_array = output_array

        
        
        self.predicted_output = np.zeros(output_array.shape)

    def feedforward(self) -> np.ndarray:
        
        
        self.layer_between_input_and_first_hidden_layer = sigmoid(
            np.dot(self.input_array, self.input_layer_and_first_hidden_layer_weights)
        )

        
        
        self.layer_between_first_hidden_layer_and_second_hidden_layer = sigmoid(
            np.dot(
                self.layer_between_input_and_first_hidden_layer,
                self.first_hidden_layer_and_second_hidden_layer_weights,
            )
        )

        
        
        self.layer_between_second_hidden_layer_and_output = sigmoid(
            np.dot(
                self.layer_between_first_hidden_layer_and_second_hidden_layer,
                self.second_hidden_layer_and_output_layer_weights,
            )
        )

        return self.layer_between_second_hidden_layer_and_output

    def back_propagation(self) -> None:

        updated_second_hidden_layer_and_output_layer_weights = np.dot(
            self.layer_between_first_hidden_layer_and_second_hidden_layer.T,
            2
            * (self.output_array - self.predicted_output)
            * sigmoid_derivative(self.predicted_output),
        )
        updated_first_hidden_layer_and_second_hidden_layer_weights = np.dot(
            self.layer_between_input_and_first_hidden_layer.T,
            np.dot(
                2
                * (self.output_array - self.predicted_output)
                * sigmoid_derivative(self.predicted_output),
                self.second_hidden_layer_and_output_layer_weights.T,
            )
            * sigmoid_derivative(
                self.layer_between_first_hidden_layer_and_second_hidden_layer
            ),
        )
        updated_input_layer_and_first_hidden_layer_weights = np.dot(
            self.input_array.T,
            np.dot(
                np.dot(
                    2
                    * (self.output_array - self.predicted_output)
                    * sigmoid_derivative(self.predicted_output),
                    self.second_hidden_layer_and_output_layer_weights.T,
                )
                * sigmoid_derivative(
                    self.layer_between_first_hidden_layer_and_second_hidden_layer
                ),
                self.first_hidden_layer_and_second_hidden_layer_weights.T,
            )
            * sigmoid_derivative(self.layer_between_input_and_first_hidden_layer),
        )

        self.input_layer_and_first_hidden_layer_weights += (
            updated_input_layer_and_first_hidden_layer_weights
        )
        self.first_hidden_layer_and_second_hidden_layer_weights += (
            updated_first_hidden_layer_and_second_hidden_layer_weights
        )
        self.second_hidden_layer_and_output_layer_weights += (
            updated_second_hidden_layer_and_output_layer_weights
        )

    def train(self, output: np.ndarray, iterations: int, give_loss: bool) -> None:
        for iteration in range(1, iterations + 1):
            self.output = self.feedforward()
            self.back_propagation()
            if give_loss:
                loss = np.mean(np.square(output - self.feedforward()))
                print(f"Iteration {iteration} Loss: {loss}")

    def predict(self, input_arr: np.ndarray) -> int:

        
        self.array = input_arr

        self.layer_between_input_and_first_hidden_layer = sigmoid(
            np.dot(self.array, self.input_layer_and_first_hidden_layer_weights)
        )

        self.layer_between_first_hidden_layer_and_second_hidden_layer = sigmoid(
            np.dot(
                self.layer_between_input_and_first_hidden_layer,
                self.first_hidden_layer_and_second_hidden_layer_weights,
            )
        )

        self.layer_between_second_hidden_layer_and_output = sigmoid(
            np.dot(
                self.layer_between_first_hidden_layer_and_second_hidden_layer,
                self.second_hidden_layer_and_output_layer_weights,
            )
        )

        return int((self.layer_between_second_hidden_layer_and_output > 0.6)[0])


def sigmoid(value: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-value))


def sigmoid_derivative(value: np.ndarray) -> np.ndarray:
    return (value) * (1 - (value))


def example() -> int:
    
    test_input = np.array(
        (
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1],
        ),
        dtype=np.float64,
    )

    
    output = np.array(([0], [1], [1], [0], [1], [0], [0], [1]), dtype=np.float64)

    
    neural_network = TwoHiddenLayerNeuralNetwork(
        input_array=test_input, output_array=output
    )

    
    
    neural_network.train(output=output, iterations=10, give_loss=False)

    return neural_network.predict(np.array(([1, 1, 1]), dtype=np.float64))


if __name__ == "__main__":
    example()
