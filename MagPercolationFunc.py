# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:40:27 2018

@author: Liam Winton
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:51:41 2018

@author: Liam
"""
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt


"""
This works in almost the exact same way as the PercolationFunc for the disease propagation.
A grid of ions within a magnetic material are simulated, with varying spin states.
Different spin states influence their neighbours, and so it is a percolating system. 
This program outputs the number of spin states in each material simulation.
"""


def MagPercolationFunc(N, L, P):
    
    counter = 0
    x_vals = np.arange(0,1,0.05)
    #x_vals = [0.2]
    final_magnetic_avg = np.array(0)

    for k in x_vals:
        
        total_magnetic = np.array(0)
        
        for p in range(L):
        
            ion_array = np.zeros((N,N))
            x = k
            
            #This section randomly selects a number of the ion_array to be magnetised
            #A magnetised ion is given a tag of 1
            for i in range(N):
                for j in range(N):
                    r = np.random.rand(1)
                    if r < x:
                        ion_array[i,j] = 1
                        
            change = 1
            while change != 0:
                
                change = 0
                
                """
                This code allows the live viewing of the propagation of the
                infection. Use for bug handling, comment out otherwise as this
                vastly slows down the speed of the program.
                """
                counter = counter + 1
                
#                if counter %2 == 0:
#                    ion_array = np.flipud(ion_array)
#                    mp.pyplot.imshow(ion_array, interpolation='none', cmap = "Vega10_r")
#                    mp.pyplot.title("Magnetic Distribution through CdMnTe")
#                    mp.pyplot.axis('off')
#                    mp.pyplot.pause(5)
#                    ion_array = np.flipud(ion_array)
#
#                else:
#                    mp.pyplot.imshow(ion_array, interpolation='none', cmap = "Vega10_r")
#                    mp.pyplot.title("Magnetic Distribution through CdMnTe")
#                    mp.pyplot.axis('off')
#                    mp.pyplot.pause(1)
                    
#                mp.pyplot.imshow(ion_array, interpolation='none', cmap = "Vega10_r")
#                mp.pyplot.title("Magnetic Distribution through CdMnTe")
#                mp.pyplot.axis('off')
#                mp.pyplot.pause(5)

                for i in range(N):
                    for j in range(N):
                        
                        
                        """
                        This section handles the interior of the matrix. 
                        Modify this section to modify the coordination number.
                        """
                        if ion_array[i,j] == 1 and i > 0 and i < N-1 and j > 0 and j < N-1:
                                                                 
                            if ion_array[i-1, j-1] == 1: 
                                ion_array[i-1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i-1, j] == 1: 
                                ion_array[i-1, j] =2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i-1, j+1] == 1: 
                                ion_array[i-1, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i, j+1] == 1: 
                                ion_array[i, j+1] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue
                                
                            if ion_array[i+1, j+1] == 1: 
                                ion_array[i+1, j+1] = 2
                                ion_array[i,j] = 2    
                                change += 1
                                continue
                                
                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j-1] == 1: 
                                ion_array[i+1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i, j-1] == 1: 
                                ion_array[i, j-1] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue

                        """
                        This section handles the top and bottom edges of the matrix
                        """
                        
                        #Top edge of the matrix
                        if ion_array[i,j] == 1 and i == 0 and j !=0 and j != N-1:
                            
                            if ion_array[i, j-1] == 1: 
                                ion_array[i, j-1] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue
                                
                            if ion_array[i, j+1] == 1: 
                                ion_array[i, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j+1] == 1: 
                                ion_array[i+1, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue
                                
                            if ion_array[i+1, j-1] == 1: 
                                ion_array[i+1, j-1] = 2
                                ion_array[i,j] = 2        
                                change += 1
                                continue
                        
                                
                        #Bottom edge of the matrix
                        if ion_array[i,j] == 1 and i == N-1 and j != 0 and j != N-1:
                            
                            if ion_array[i-1, j+1] == 1:  
                                ion_array[i-1, j+1] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue
                                
                            if ion_array[i, j+1] == 1:   
                                ion_array[i, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i, j-1] == 1:  
                                ion_array[i, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i-1, j-1] == 1:  
                                ion_array[i-1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i-1, j] == 1: 
                                ion_array[i-1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                       
                        """
                        This section handles the left and right sides of the matrix
                        """
                        
                        #Left side of the matrix
                        if ion_array[i,j] == 1 and i > 0 and i < N-1 and j == 0:
                            
                            if ion_array[i-1, j] == 1:  
                                ion_array[i-1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i-1, j+1] == 1: 
                                ion_array[i-1, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue
                                
                            if ion_array[i+1, j+1] == 1: 
                                ion_array[i+1, j+1] = 2
                                ion_array[i,j] = 2         
                                change += 1
                                continue

                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue

                        #Right side of the matrix
                        if ion_array[i,j] == 1 and i > 0 and i < N-1 and j == N-1:
                            
                            if ion_array[i-1, j] == 1: 
                                ion_array[i-1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i+1, j-1] == 1: 
                                ion_array[i+1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i, j-1] == 1: 
                                ion_array[i, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i-1, j-1] == 1: 
                                ion_array[i-1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                        """
                        This section handles the corners of the matrix
                        """
                                
                        #Top left corner
                        if ion_array[i,j] == 1 and i == 0 and j == 0:
                            
                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i+1, j+1] == 1: 
                                ion_array[i+1, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i, j+1] == 1: 
                                ion_array[i, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                        #Top right corner        
                        if ion_array[i,j] == 1 and i == 0 and j == N-1 :
                            
                            if ion_array[i, j-1] == 1: 
                                ion_array[i, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j-1] == 1: 
                                ion_array[i+1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i+1, j] == 1: 
                                ion_array[i+1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                         #Bottom left corner
                        if ion_array[i,j] == 1 and i == N-1 and j == 0:
                            
                            if ion_array[i-1, j] == 1: 
                                ion_array[i-1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i-1, j+1] == 1: 
                                ion_array[i-1, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                            if ion_array[i, j+1] == 1: 
                                ion_array[i, j+1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                                
                        #Bottom right corner
                        if ion_array[i,j] == 1 and i == N-1 and j == N-1:
                            
                            if ion_array[i-1, j] == 1: 
                                ion_array[i-1, j] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i, j-1] == 1: 
                                ion_array[i, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                            if ion_array[i-1, j-1] == 1: 
                                ion_array[i-1, j-1] = 2
                                ion_array[i,j] = 2
                                change += 1
                                continue
                            
                        #This is where a loop back mechanism would go (if I had one)
                #Put it here
                #ion_array = np.flipud(ion_array)

                                
            total_magnetic_x = 0
            #infection_rate = np.array(0)
            for i in range(N):
                for j in range(N):
                    if ion_array[i,j] == 1:
                        total_magnetic_x += 1
                        
            total_magnetic = np.append(total_magnetic, total_magnetic_x)
            #infection_rate = np.append( infection_rate, (total_infected / (1-k) ) )
            
                        
        final_magnetic_avg = np.append(final_magnetic_avg, (np.average(total_magnetic[1:,])))
        
    return ion_array, final_magnetic_avg#, infection_rate