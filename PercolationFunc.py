# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:51:41 2018

@author: Liam Winton 
"""
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

"""
This function is used with the Percolation Systems file.
This program simulates disease spreading throughout a population.
This function generates a grid that is used to represent a population.
A certain number of these individuals are "immune" from disease.
    The proportion of the population infected is varied by input parameters
    
The rest are healthy but can be "infected".
1 or more individuals start with the disease, depending on the input. The individual is random.

The function checks each individual and its neighbours and infects any unimmune individuals
    If the coordination number is high, an individual will spread disease to its neighbour's neighbours.
        This is to simulate a more or less social population

As the function iterates through the matrix it is clear that it spreads down very rapidly but up very slowly. 
    This was fixed by flipping the matrix at each total iteration, so the disease spreads faster when viewing.
        Note that in the assignment, time of spread was not a concern and so there is no real time element in this program.
            The timing and spread rate are purely for testing and visual purposes. 
                The goal in this program is to determine how many are infected after all possible infections occur.

The total number of infected/immune are output.
"""

def PercolationFunc(N, L, P, T):
    
    counter = 0
    #x_vals = np.arange(0,1,0.05)
    x_vals = [0.4, 0.5]
    final_infected_avg = np.array(0)

    for k in x_vals:
        
        total_infected = np.array(0)
        
        for p in range(L):
        
            population = np.zeros((N,N))
            x = k
            
            #This section randomly selects a number of the population to be immunised
            #An immune individual is given a tag of 2
            for i in range(N):
                for j in range(N):
                    r = np.random.rand(1)
                    if r < x:
                        population[i,j] = 2
                        
                        
            #This section selects the coordinates of an individual who will be the first infected
            #If this individual is immune then it is overriden and is then infected   
            #An infected individual is given a tag of 1
            for i in range(P):
                patient_zero_x = np.random.randint(N)
                patient_zero_y = np.random.randint(N)
                population[patient_zero_y, patient_zero_x] = 1
                change = 1
            
            #This section checks the value of each position in the matrix
            #If a position is infected, it's neighbours are checked 
            #If a neighbour is uninfected, they become infected
            #This section only covers the inside of the matrix, the edges are not checked
            
            while change != 0:
                
                change = 0
                
                """
                This code allows the live viewing of the propagation of the
                infection. Use for bug handling, comment out otherwise as this
                vastly slows down the speed of the program.
                """
                counter = counter + 1
                
                if counter %2 == 0:
                    population = np.flipud(population)
                    mp.pyplot.imshow(population, interpolation='none', cmap = "Vega10_r")
                    mp.pyplot.title("Disease Propagation Through A Population")
                    mp.pyplot.axis('off')
                    mp.pyplot.pause(15)
                    population = np.flipud(population)

                else:
                    mp.pyplot.imshow(population, interpolation='none', cmap = "Vega10_r")
                    mp.pyplot.title("Disease Propagation Through A Population")
                    mp.pyplot.axis('off')
                    mp.pyplot.pause(15)


                for i in range(N):
                    for j in range(N):
                        
                        
                        """
                        This section handles the interior of the matrix. 
                        Modify this section to modify the coordination number.
                        """
                        if population[i,j] == 1 and i > 0 and i < N-1 and j > 0 and j < N-1 and (T == 0 or T == 2):
                            
                            population[i,j] == 3
                            r = np.random.rand(1)

                            #Coordination number of 8: Standard case
                            if population[i-1, j-1] == 0: 
                                population[i-1, j-1] = 1
                                change += 1
                            if population[i-1, j] == 0: 
                                population[i-1, j] =1
                                change += 1
                            if population[i-1, j+1] == 0: 
                                population[i-1, j+1] = 1
                                change += 1
                            if population[i, j+1] == 0: 
                                population[i, j+1] = 1
                                change += 1
                            if population[i+1, j+1] == 0: 
                                population[i+1, j+1] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j-1] == 0: 
                                population[i+1, j-1] = 1
                                change += 1
                            if population[i, j-1] == 0: 
                                population[i, j-1] = 1
                                change += 1

                        
                        #Unsociable Case: Randomly infect some neighbours
                        if population[i,j] == 1 and i > 0 and i < N-1 and j > 0 and j < N-1 and T == 1:
                            
                            if population[i-1, j-1] == 0 and r > 0.5: 
                                population[i-1, j-1] = 1
                                change += 1
                            if population[i-1, j] == 0 and r < 0.5: 
                                population[i-1, j] =1
                                change += 1
                            if population[i-1, j+1] == 0 and r > 0.5: 
                                population[i-1, j+1] = 1
                                change += 1
                            if population[i, j+1] == 0 and r < 0.5: 
                                population[i, j+1] = 1
                                change += 1
                            if population[i+1, j+1] == 0 and r > 0.5: 
                                population[i+1, j+1] = 1
                                change += 1
                            if population[i+1, j] == 0 and r < 0.5: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j-1] == 0 and r > 0.5: 
                                population[i+1, j-1] = 1
                                change += 1
                            if population[i, j-1] == 0  and r < 0.5: 
                                population[i, j-1] = 1
                                change += 1
                                
                        #Sociable Case: Infects more than nearest neighbours
                        if population[i,j] == 1 and i > 1 and i < N-2 and j > 1 and j < N-2 and T == 2:
                            
                            population[i,j] == 3
                            r = np.random.rand(1)
                            
                            if population[i-1, j-1] == 0: 
                                population[i-1, j-1] = 1
                                change += 1
                            if population[i-1, j] == 0: 
                                population[i-1, j] =1
                                change += 1
                            if population[i-1, j+1] == 0: 
                                population[i-1, j+1] = 1
                                change += 1
                            if population[i, j+1] == 0: 
                                population[i, j+1] = 1
                                change += 1
                            if population[i+1, j+1] == 0: 
                                population[i+1, j+1] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j-1] == 0: 
                                population[i+1, j-1] = 1
                                change += 1
                            if population[i, j-1] == 0: 
                                population[i, j-1] = 1
                                change += 1
                                
                            #Extended Range of infection    
                                
                            if population[i-2, j-2] == 0: 
                                population[i-2, j-2] = 1
                                change += 1
                                
                            if population[i-2, j-1] == 0: 
                                population[i-2, j-1] = 1
                                change += 1
                                                                
                            if population[i-2, j] == 0: 
                                population[i-2, j] = 1
                                change += 1
                                                                
                            if population[i-2, j+1] == 0: 
                                population[i-2, j+1] = 1
                                change += 1
                                                                
                            if population[i-2, j+2] == 0: 
                                population[i-2, j+2] = 1
                                change += 1
                                                                                                
                            if population[i-1, j+2] == 0: 
                                population[i-1, j+2] = 1
                                change += 1
                                                                                                
                            if population[i, j+2] == 0: 
                                population[i, j+2] = 1
                                change += 1
                                                                                            
                            if population[i+1, j+2] == 0: 
                                population[i+1, j+2] = 1
                                change += 1
                                                                                                
                            if population[i+2, j+2] == 0: 
                                population[i+2, j+2] = 1
                                change += 1
                                                                                            
                            if population[i+2, j+1] == 0: 
                                population[i+2, j+1] = 1
                                change += 1
                                                                                            
                            if population[i+2, j] == 0: 
                                population[i+2, j] = 1
                                change += 1
                                                                                            
                            if population[i+2, j-1] == 0: 
                                population[i+2, j-1] = 1
                                change += 1
                                                                                                
                            if population[i+2, j-2] == 0: 
                                population[i+2, j-2] = 1
                                change += 1
                                                                                            
                            if population[i+1, j-2] == 0: 
                                population[i+1, j-2] = 1
                                change += 1
                                                                                            
                            if population[i, j-2] == 0: 
                                population[i, j-2] = 1
                                change += 1
                                                                                                
                            if population[i-1, j-2] == 0: 
                                population[i-1, j-2] = 1
                                change += 1
                        """
                        This section handles the top and bottom edges of the matrix
                        """
                        
                        #Top edge of the matrix
                        if population[i,j] == 1 and i == 0 and j !=0 and j != N-1:
                            
                            if population[i, j-1] == 0: 
                                population[i, j-1] = 1
                                change += 1
                            if population[i, j+1] == 0: 
                                population[i, j+1] = 1
                                change += 1
                            if population[i+1, j+1] == 0: 
                                population[i+1, j+1] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j-1] == 0: 
                                population[i+1, j-1] = 1
                                change += 1
                        
                                
                        #Bottom edge of the matrix
                        if population[i,j] == 1 and i == N-1 and j != 0 and j != N-1:
                            
                            if population[i-1, j+1] == 0:  
                                population[i-1, j+1] = 1
                                change += 1
                            if population[i, j+1] == 0:   
                                population[i, j+1] = 1
                                change += 1
                            if population[i, j-1] == 0:  
                                population[i, j-1] = 1
                                change += 1
                            if population[i-1, j-1] == 0:  
                                population[i-1, j-1] = 1
                                change += 1
                            if population[i-1, j] == 0: 
                                population[i-1, j] = 1
                                change += 1
                       
                        """
                        This section handles the left and right sides of the matrix
                        """
                        
                        #Left side of the matrix
                        if population[i,j] == 1 and i > 0 and i < N-1 and j == 0:
                            
                            if population[i-1, j] == 0:  
                                population[i-1, j] = 1
                                change += 1 
                            if population[i-1, j+1] == 0: 
                                population[i-1, j+1] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j+1] == 0: 
                                population[i+1, j+1] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                        #Right side of the matrix
                        if population[i,j] == 1 and i > 0 and i < N-1 and j == N-1:
                            
                            if population[i-1, j] == 0: 
                                population[i-1, j] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j-1] == 0: 
                                population[i+1, j-1] = 1
                                change += 1
                            if population[i, j-1] == 0: 
                                population[i, j-1] = 1
                                change += 1
                            if population[i-1, j-1] == 0: 
                                population[i-1, j-1] = 1
                                change += 1
                                
                        """
                        This section handles the corners of the matrix
                        """
                                
                        #Top left corner
                        if population[i,j] == 1 and i == 0 and j == 0:
                            
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1
                            if population[i+1, j+1] == 0: 
                                population[i+1, j+1] = 1
                                change += 1
                            if population[i, j+1] == 0: 
                                population[i, j+1] = 1
                                change += 1
                        #Top right corner        
                        if population[i,j] == 1 and i == 0 and j == N-1 :
                            
                            if population[i, j-1] == 0: 
                                population[i, j-1] = 1
                                change += 1
                            if population[i+1, j-1] == 0: 
                                population[i+1, j-1] = 1
                                change += 1
                            if population[i+1, j] == 0: 
                                population[i+1, j] = 1
                                change += 1     
                            
                         #Bottom left corner
                        if population[i,j] == 1 and i == N-1 and j == 0:
                            
                            if population[i-1, j] == 0: 
                                population[i-1, j] = 1
                                change += 1
                            if population[i-1, j+1] == 0: 
                                population[i-1, j+1] = 1
                                change += 1
                            if population[i, j+1] == 0: 
                                population[i, j+1] = 1
                                change += 1
                        #Bottom right corner
                        if population[i,j] == 1 and i == N-1 and j == N-1:
                            
                            if population[i-1, j] == 0: 
                                population[i-1, j] = 1
                                change += 1
                            if population[i, j-1] == 0: 
                                population[i, j-1] = 1
                                change += 1
                            if population[i-1, j-1] == 0: 
                                population[i-1, j-1] = 1
                                change += 1
                                
                        #This is where a loop back mechanism would go (if I had one)
                #Put it here
                population = np.flipud(population)

                                
            total_infected_x = 0
            #infection_rate = np.array(0)
            for i in range(N):
                for j in range(N):
                    if population[i,j] == 1:
                        total_infected_x += 1
                        
            total_infected = np.append(total_infected, total_infected_x)
            #infection_rate = np.append( infection_rate, (total_infected / (1-k) ) )
            
                        
        final_infected_avg = np.append(final_infected_avg, (np.average(total_infected[1:,])))
        
    return population, final_infected_avg#, infection_rate