# -*- coding: utf-8 -*-
"""
EG21007  - Introduction To Programming
Assignment 5 - Damped Linear Harmonic Oscillator
@author: Liam Winton
"""

"""
This program calculates the motion over time of damped harmonic oscillators using
matrix methods.
Task (a) refers to an undamped oscillator, which will continue oscillating 
indefinitely due to nothing slowing it down.
Task (b) refers to an overdamped oscillator, which does not oscillate at all and
returns to its equilibrium point almost immediately. 
Task (c) is a damped oscillator that is neither over- or under-damped. 
"""


import numpy as np
import pylab as plt
#defining variables common to each calculation
k = 10
m = 1
N = 10000
delta_t = 0.001 
v_t = 0
x_t = 0.1

#setting up a matrix to store x_t and v_t at each time increment
vxt_matrix = np.zeros([N,2])
vxt_matrix[0] = 0,0.1

#defining a function that computes the velocity and position at each time increment and stores them within the matrix
def v(v_t,x_t):
    
    v = v_t + ((-1 * mu/m)*v_t - (k/m)*x_t)*delta_t
    x = x_t + v*delta_t
    
    return(v,x)
    
#creating an array of time values suitable for use on an x axis    
t= np.linspace(0,10,N)

#Task (a). 
mu = 0

for i in range(1,N):
    vxt_matrix[i] = v(vxt_matrix[i-1,0],vxt_matrix[i-1,1])
plt.plot(t,vxt_matrix[:,1],'r',linewidth = 2,label='$\mu = 0$')

#Task (b)
mu = 2 * np.sqrt(m*k)

for i in range(1,N):
    vxt_matrix[i] = v(vxt_matrix[i-1,0],vxt_matrix[i-1,1])
plt.plot(t,vxt_matrix[:,1],'g',linewidth = 2, label = '$\mu = 2\sqrt{mk}$')

#Task (c)
mu = 0.25 * np.sqrt(m*k)

for i in range(1,N):
    vxt_matrix[i] = v(vxt_matrix[i-1,0],vxt_matrix[i-1,1])
plt.plot(t,vxt_matrix[:,1],linewidth = 2,label = '$\mu$ = $\\frac{1}{4}$ $\sqrt{mk}$')

#formatting x axis
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.xlabel('Time (s)',fontsize = 20)

#formatting y axis
plt.ylabel('Displacement (m)',fontsize = 20)
#general graphical formatting
plt.legend(loc = 'upper right')
plt.title('Damped Harmonic Oscillator', fontsize = 20)
