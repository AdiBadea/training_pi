w1 = 1
w2 = 1
b  = 1

i1 = 1
i2 = 1

neuronOut = ((w1 * i1) + (w2 * i2)) + b

print(neuronOut)

def sigmoid(x):
# Functia de activare: f(x) = 1 / (1 + e^(-x))
return 1 / (1 + np.exp(-x))

print(sigmoid(neuronOut))