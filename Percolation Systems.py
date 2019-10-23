"""
06/10/2018 - PH51001 Computational Physics II
Class topic: Percolation Systems

Author: Liam Winton
"""
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from PercolationFunc import PercolationFunc
from MagPercolationFunc import MagPercolationFunc

#This program simulates virus propagation through a human population comprising
#immune individuals and non immune individuals. Infected individuals are chosen at random.
#The system runs until there are no new individuals being infected, as the propagation has stopped.


"""
This sets the size of the side of the square population matrix and the range
of immunised people as a fraction of the total population (from 0 to 1).
"""
N = 100   #Side Size
x_vals = np.arange(0,1,0.05)

"""
This is for Problems 1 and 2 of the assignment. The propagation function is called
to simulate the spreading of a disease through an arbitrary population matrix. 
The size of the matrix is given as N, the second parameter is the number of
iterations the program will perform, the third value is the initial number
of infection sources, and the fourth parameter is a number indicating the 
sociability of the population. 0 is standard coordination number of 8, 1 is for
coordination number < 8, and 2 is for coordination number > 8.
A plot is then made of the number of infected against the rate of immunisation 
(x values). This is a weighted statistical average 
over the outputs of the percolation function. 

Note that much code is repeated due to requiring specific plots for assignment writeups.
This code can be easily adapted using for loops to create a more compact simulation.
Graphs are produced of the number of infected against immunity rate.

This can be used to determine at what threshold of immunisation does herd immunity become important
    and why anti-vaxxers pose a problem for those unable to get vaccinated.
    
The same principles can also be applied in Section 5 to simulate a critical threshold that
    a magnetic material goes through to become permanently magnetized via a cascading effect
        of spin states. 
"""
(population, final_infected_avg10) = PercolationFunc(N, 10, 1, 0)
#(population, final_infected_avg1000) = PercolationFunc(N, 1000, 1, 0)
#     
#
#plt.plot(x_vals, final_infected_avg10[1:,], '-.',label = "10 simulations")
#plt.plot(x_vals, final_infected_avg1000[1:,], 'r:',label = "1000 simulations")
#
#plt.xlabel("Proportion Immunised")
#plt.ylabel("Number Infected")
#plt.legend(loc = "upper right")
#plt.title("Number of infected people against rate of immunisation")



#Problem 2(b) : 6.7 & 6.5
#(population, final_infected_avg10) = PercolationFunc(N, 1000, 1, 0)
#print("10x10")
#(population, final_infected_avg12) = PercolationFunc(12, 1000, 1, 0)
#print("12x12")
#(population, final_infected_avg14) = PercolationFunc(14, 1000, 1, 0)
#print("14x14")
#(population, final_infected_avg16) = PercolationFunc(16, 1000, 1, 0)
#print("16x16")
#(population, final_infected_avg20) = PercolationFunc(20, 1000, 1, 0)

#infection_rate10 = (final_infected_avg10[1:,] / ( (1 - x_vals) * N**2) )
#infection_rate12 = (final_infected_avg12[1:,] / ( (1 - x_vals) * 12**2) )
#infection_rate14 = (final_infected_avg14[1:,] / ( (1 - x_vals) * 14**2) )
#infection_rate16 = (final_infected_avg16[1:,] / ( (1 - x_vals) * 16**2) )
#infection_rate20 = (final_infected_avg20[1:,] / ( (1 - x_vals) * 20**2) )
#
#
#plt.plot(x_vals, infection_rate10, label = '10x10')
#plt.plot(x_vals, infection_rate12, label = '12x12')
#plt.plot(x_vals, infection_rate14, label = '14x14')
#plt.plot(x_vals, infection_rate16, label = '16x16')
#plt.plot(x_vals, infection_rate20, label = '20x20')



#prop_imm10 = final_infected_avg10[1:,] / N**2
#prop_imm12 = final_infected_avg12[1:,] / 12**2
#prop_imm14 = final_infected_avg14[1:,] / 14**2
#prop_imm16 = final_infected_avg16[1:,] / 16**2
#prop_imm20 = final_infected_avg20[1:,] / 20**2
#
#plt.plot(x_vals, prop_imm10, label = "10x10")
#plt.plot(x_vals, prop_imm12, label = "12x12")
#plt.plot(x_vals, prop_imm14, label = "14x14")
#plt.plot(x_vals, prop_imm16, label = "16x16")
#plt.plot(x_vals, prop_imm20, label = "20x20")



#Problem 2(b): 6.8
#(population, final_infected_avg10) = PercolationFunc(N, 1000, 1, 0)
#print("10x10")
#(population, final_infected_avg20) = PercolationFunc(20, 1000, 1, 0)
#print("20x20")
#(population, final_infected_avg30) = PercolationFunc(30, 1000, 1, 0)
#print("30x30")
#(population, final_infected_avg40) = PercolationFunc(40, 1000, 1, 0)
#print("40x40")
#(population, final_infected_avg50) = PercolationFunc(50, 1000, 1, 0)
#
#infection_rate10 = (final_infected_avg10[1:,] / ( (1 - x_vals) * N**2) )
#infection_rate20 = (final_infected_avg20[1:,] / ( (1 - x_vals) * 20**2) )
#infection_rate30 = (final_infected_avg30[1:,] / ( (1 - x_vals) * 30**2) )
#infection_rate40 = (final_infected_avg40[1:,] / ( (1 - x_vals) * 40**2) )
#infection_rate50 = (final_infected_avg50[1:,] / ( (1 - x_vals) * 50**2) )
#
#plt.plot(x_vals, infection_rate10, label = '10x10')
#plt.plot(x_vals, infection_rate20, label = '20x20')
#plt.plot(x_vals, infection_rate30, label = '30x30')
#plt.plot(x_vals, infection_rate40, label = '40x40')
#plt.plot(x_vals, infection_rate50, label = '50x50')



#6.6

#prop_imm10 = final_infected_avg10[1:,] / N**2
#prop_imm20 = final_infected_avg20[1:,] / 20**2
#prop_imm30 = final_infected_avg30[1:,] / 30**2
#prop_imm40 = final_infected_avg40[1:,] / 40**2
#prop_imm50 = final_infected_avg50[1:,] / 50**2
#
#
#plt.plot(x_vals, prop_imm10, label = '10x10')
#plt.plot(x_vals, prop_imm20, label = '20x20')
#plt.plot(x_vals, prop_imm30, label = '30x30')
#plt.plot(x_vals, prop_imm40, label = '40x40')
#plt.plot(x_vals, prop_imm50, label = '50x50')

#
#plt.ylim(0,1.1)
#plt.xlabel("Proportion Immunised")
#plt.ylabel("Infection Rate")
#plt.title("Infection rate against rate of immunisation")
#plt.legend(loc = "upper right")

"""
This section calculates and plots for Problem 3 of the assignment. A number
of initial infected is passed into the function and the averaged rate of infection
is calculated over a series of immunisation values (x values). The third 
parameter passing into the function is the number of sources of infection.
""" 

#(population, final_infected_sources1) = PercolationFunc(N, 1000, 1, 0)
#print("1")
#(population, final_infected_sources2) = PercolationFunc(N, 1000, 2, 0)
#print("2")
#(population, final_infected_sources3) = PercolationFunc(N, 1000, 3, 0)
#print("3")
#(population, final_infected_sources4) = PercolationFunc(N, 1000, 4, 0)
#print("4")
#(population, final_infected_sources5) = PercolationFunc(N, 1000, 5, 0)
#
#infection_rate1 = (final_infected_sources1[1:,] / ( (1 - x_vals) * N**2) )
#infection_rate2 = (final_infected_sources2[1:,] / ( (1 - x_vals) * N**2) )
#infection_rate3 = (final_infected_sources3[1:,] / ( (1 - x_vals) * N**2) )
#infection_rate4 = (final_infected_sources4[1:,] / ( (1 - x_vals) * N**2) )
#infection_rate5 = (final_infected_sources5[1:,] / ( (1 - x_vals) * N**2) )
#
#plt.plot(x_vals, infection_rate1, '-'  ,label = "1 Source")
#plt.plot(x_vals, infection_rate2, '-'  ,label = "2 Sources")
#plt.plot(x_vals, infection_rate3, '--' ,label = "3 Sources")
#plt.plot(x_vals, infection_rate4, '-.' ,label = "4 Sources")
#plt.plot(x_vals, infection_rate5, ':'  ,label = "5 Sources")
#
#plt.xlabel("Proportion Immunised")
#plt.ylabel("Infection Rate")
#plt.legend(loc = "lower right")
#plt.title("Infection rate against rate of immunisation")
#plt.ylim(0,1)


"""
Part 4 of the assignment. This part of the program simulates sociable vs
unsociable societies, corresponding to the ease at which the disease spreads
through the population. Instead of infecting all 8 individuals around an 
infected individual, less than 8 are infected in the unsociable case. In the
sociable case, more than 8 people are infected around the infected individual. 
"""

#(population, final_infected_c8) = PercolationFunc(N, 1000, 1, 1)
#infection_rate_c8 = (final_infected_c8[1:,] / ( (1 - x_vals) * N**2) )
#plt.plot(x_vals, infection_rate_c8, label = 'Coordination Number < 8')
#
#
#
#(population, final_infected_c12) = PercolationFunc(N, 1000, 1, 2)
#infection_rate_c12 = (final_infected_c12[1:,] / ( (1 - x_vals) * N**2) )
#plt.plot(x_vals, infection_rate_c12, label = 'Coordination Number > 8')
#
#
#
#
#plt.ylim(0,1.1)
#plt.xlabel("Proportion Immunised")
#plt.ylabel("Infection Rate")
#plt.title("Infection rate against rate of immunisation")
#plt.legend(loc = "upper right")

"""
Part 5: Using a Percolation function to simulate a magnetic material
"""

#(ion_array, final_magnetic) = MagPercolationFunc(N, 1000, 1)
#
#unpaired_mag_perc = (final_magnetic[1:,] / N**2) * 100
#
#plt.plot(x_vals, unpaired_mag_perc )
#
#plt.ylim(0,10)
#plt.xlabel("Concentration of magnetic ions")
#plt.ylabel("Effective Concentration of unpaired spins [%]")
#plt.title("Infection rate against rate of immunisation")
#plt.legend(loc = "upper right")