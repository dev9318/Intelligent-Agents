import numpy as np
import matplotlib.pyplot as plt


def sigmoid (x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expected_output = np.array([[0],[1],[1],[0]])


epochs = 10000
lr = 0.1


hidden_weights = np.random.uniform(size=(2,2))
hidden_bias =np.random.uniform(size=(1,2))
output_weights = np.random.uniform(size=(2,1))
output_bias = np.random.uniform(size=(1,1))


errors=[]
x=[]


#Training algorithm
for i in range(epochs):

    x.append(i)
        
    #Forward Propagation
    #1st layer
    hidden_layer_activation = np.dot(inputs,hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    # 2nd layer
    output_layer_activation = np.dot(hidden_layer_output,output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)


    #Backpropagation
    #2nd layer
    error = expected_output - predicted_output
    errors.append(error[0])
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    #1st layer
    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
	

    #Updating Weights and Biases
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
    output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
    hidden_weights += inputs.T.dot(d_hidden_layer) * lr
    hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr


plt.plot(x,errors)
plt.xlabel("No. of Iterations")
plt.ylabel("Error")
plt.show()
