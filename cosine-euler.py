#Numerical solution of a cosine differential equation
import numpy as np
import math
import matplotlib.pyplot as plt

# Set parameters for Euler's method
h = 0.01
a = 0
b = 10
N = int( (b-a)/h)

#initialize our arrays
w = np.zeros(N)
x = np.zeros(N)
Analytic_Solution = np.zeros(N)

#Initial Conditions
w[0] = 1.0
x[0] = 0
Analytic_Solution[0] = 1.0

#For loop to numerically solve the diffy eqn with Euler's Method
for i in range(1,N):
    w[i] = w[i-1] + h * math.sin(x[i-1])
    x[i] = x[i-1] + h
    Analytic_Solution[i] = 2.0 - math.cos(x[i])

#Create graph
fig = plt.figure(figsize = (8,4))

#---leftmost plot (numerical solution)
ax = fig.add_subplot(1,3,1)
plt.plot(x,w,color='red')
plt.title('Numerical Solution')

#---middle plot (analytic solution)
ax = fig.add_subplot(1,3,2)
plt.plot(x,Analytic_Solution,color='blue')
plt.title('Analytic Solution')

#---rightmost plot (error)
ax = fig.add_subplot(1,3,3)
plt.plot(x,Analytic_Solution - w, color='green')
plt.title('Error')

fig.suptitle('Sine Solution',fontsize=20)
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()