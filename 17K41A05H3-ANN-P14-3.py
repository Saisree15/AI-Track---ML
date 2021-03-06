import pandas as pd
import numpy as np
data=pd.read_csv("C:LoadDatainKW.csv")
data.head()
data.shape

x=data[:,:4]
y=data[:,4]

normalized_datax=(x-x.mean())/x.std()
normalized_datax

normalized_datay=(y-y.mean())/y.std()
normalized_datay

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(normalized_datax,normalized_datay,test_size = 0.10, random_state = 42)

def define_structure(X, Y):
    input_unit = X.shape[0] 
    hidden_unit = 2394 # (1.5*1596)
    output_unit = Y.shape[0] 
    return (input_unit, hidden_unit, output_unit)
(input_unit, hidden_unit, output_unit) = define_structure(X_train, y_train)
print("The size of the input layer is:  = " + str(input_unit))
print("The size of the hidden layer is:  = " + str(hidden_unit))
print("The size of the output layer is:  = " + str(output_unit))

def parameters_initialization(input_unit, hidden_unit, output_unit):
    np.random.seed(2) 
    W1 = np.random.randn(hidden_unit, input_unit)*0.01
    b1 = np.zeros((hidden_unit, 1))
    W2 = np.random.randn(output_unit, hidden_unit)*0.01
    b2 = np.zeros((output_unit, 1))
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters

def sigmoid(z):
    return 1/(1+np.exp(-z))
def forward_propagation(X, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    cache = {"Z1": Z1,"A1": A1,"Z2": Z2,"A2": A2}
    
    return A2, cache

def cross_entropy_cost(A2, Y, parameters):
    m = Y.shape[1] 
    logprobs = np.multiply(np.log(A2), Y) + np.multiply((1-Y), np.log(1 - A2))
    cost = - np.sum(logprobs) / m
    cost = float(np.squeeze(cost))
                                    
    return cost

def backward_propagation(parameters, cache, X, Y):
    #number of training example
    m = X.shape[1]
    
    W1 = parameters['W1']
    W2 = parameters['W2']
    A1 = cache['A1']
    A2 = cache['A2']
   
    dZ2 = A2-Y
    dW2 = (1/m) * np.dot(dZ2, A1.T)
    db2 = (1/m) * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
    dW1 = (1/m) * np.dot(dZ1, X.T) 
    db1 = (1/m)*np.sum(dZ1, axis=1, keepdims=True)
    
    grads = {"dW1": dW1, "db1": db1, "dW2": dW2,"db2": db2}
    
    return grads

def h(a,b,x): 
    return a*x+b

def mse(a,b,x,y): 
    return np.mean((h(a,b,x) - y)**2)
def gradient(a,b,x,y): 
    return np.mean(x*(a*x+b-y), axis=-1), np.mean(a*x+b-y, axis=-1)

def rmsprop_gradient_descent(a, b, x, y, lr=1e-5, gamma=0.9, epsilon=1e-4):
    prev_error = 0
    rmsprop_a = 0
    rmsprop_b = 0
    error = np.array([])
    while True:
        gradient_a, gradient_b = gradient(a, b, x, y)
#         print(abs(mse(a, b, x, y) - prev_error))
        if abs(mse(a, b, x, y) - prev_error) < epsilon:
            break
        prev_error = mse(a, b, x, y)
        error = np.insert(error, len(error), prev_error)

        rmsprop_a = gamma * rmsprop_a + (1-gamma) * (gradient_a**2)
        rmsprop_b = gamma * rmsprop_b + (1-gamma) * (gradient_b**2)
        a -= (lr / (rmsprop_a**0.5 + 1e-8)) * gradient_a
        b -= (lr / (rmsprop_b**0.5 + 1e-8)) * gradient_b
    return a, b, error

m = 1 #Initial value of slope
c = -1 #Initial value of intercept
lr = 0.01 #Learning Rate
delta_m = 1 #Initialising Δm
delta_c = 1 #Initialising Δc
max_iters = 1000 #Maximum number of iterations  
iters_count = 0 #Counting Iterations

def deriv(m_f, c_f, datax, datay):
  m_deriv = 0
  c_deriv = 0
  for i in range(datax.shape[0]):
    x, y = datax[i], datay[i]
    m_deriv += (y-m_f*x-c_f)*x
    c_deriv += (y-m_f*x-c_f)
  m_deriv = -m_deriv/len(datax)
  c_deriv = -c_deriv/len(datay)
  return m_deriv, c_deriv  


while iters_count < max_iters:
  delta_m, delta_c = deriv(m, c, x_train, y_train)
  delta_m = -lr * delta_m
  delta_c = -lr * delta_c
  m += delta_m
  c += delta_c
  iters_count += 1
  print(f"Iteration: {iters_count}\tValue of m: {m}, \tValue of c: {c}")

print(f"\nThe local minima occurs at: {m}, {c}")

def neural_network_model(X, Y, hidden_unit, num_iterations = 1000):
    np.random.seed(3)
    input_unit = define_structure(X, Y)[0]
    output_unit = define_structure(X, Y)[2]
    
    parameters = parameters_initialization(input_unit, hidden_unit, output_unit)
   
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    for i in range(0, num_iterations):
        A2, cache = forward_propagation(X, parameters)
        cost = cross_entropy_cost(A2, Y, parameters)
        grads = backward_propagation(parameters, cache, X, Y)
        parameters = rmsprop_gradient_descent(parameters, grads)
        if i % 5 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
    return parameters
parameters = neural_network_model(X_train, y_train, 4, num_iterations=1000)

def prediction(parameters, X):
    A2, cache = forward_propagation(X, parameters)
    predictions = np.round(A2)
    
    return predictions

predictions = prediction(parameters, X_train)
print ('Accuracy Train: %d' % float((np.dot(y_train, predictions.T) + np.dot(1 - y_train, 1 - predictions.T))/float(y_train.size)*100) + '%')
predictions = prediction(parameters, X_test)
print ('Accuracy Test: %d' % float((np.dot(y_test, predictions.T) + np.dot(1 - y_test, 1 - predictions.T))/float(y_test.size)*100) + '%')
