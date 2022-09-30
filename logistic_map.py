import numpy as np 
import matplotlib.pyplot as plt 

def logistic_map(r, x):
	'''a function to calculate the next step of the discrete map.  Inputs
	x and y are transformed to x_next, y_next respectively'''
	x_next = x * r * (1 - x)
	r_next = r + 0.000001
	return r_next, x_next

steps = 3000000

X = np.zeros(steps + 1)
R = np.zeros(steps + 1)

R[0], X[0] = 1, 0.5

# map the equation to array step by step using the logistic_map function above
for i in range(steps):
	r_next, x_next = (logistic_map(R[i], X[i])) # calls the logistic_map function on X[i] as x and Y[i] as y
	R[i+1] = r_next
	X[i+1] = x_next

plt.style.use('dark_background')
plt.figure(figsize=(10, 10))
plt.plot(R, X, '^', color='white', alpha=0.4, markersize = 0.013)
plt.axis('on')
plt.show()