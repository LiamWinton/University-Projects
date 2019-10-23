# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:20:15 2017

@author: Liam
"""

"""
This program simulates Bragg reflector characteristics with different materials.

Understanding Bragg reflectors is important in the application of wave guides,
particularly optical cabling.

The program prompts the user to input the stack material and gives a sample 
table of materials. The number is stacks is prompted.
The angle of the incoming radiation is also prompted, and a graph is produced that
describes the reflectivity of the reflector as a function of the number of material 
stacks. 

Wavelength has been hard coded in this form of the program but it can also be prompted
by commenting out line 129 and uncommenting line 122. Wavelength is entered in nanometers.

This program was produced as part of an Optics module. It uses an index and a
matrix method to perform the calculations.
"""


import numpy as np
import matplotlib.pyplot as plt


# PH41005 Optics and Photonics
# Assignment 3 - Bragg Reflector


# Function that calculates the reflectivity for a particular set of N values
def ReflectionCalculatorFunction(n_h, n_l, n_s, N, wavelength, angle, wav_range):
    # CALCULATING THETA
    theta1 = angle * np.pi / 180
    theta2 = np.arcsin(1.0 * np.sin(theta1) / n_h)
    theta3 = np.arcsin(n_h * np.sin(theta2 / n_l))
    theta_s = np.arcsin(n_l * np.sin(theta3) / n_s)

    # CALCUTING h values
    h_2 = wavelength / (4 * n_h)
    h_3 = wavelength / (4 * n_l)

    # CALCULATING P
    p1 = 1 * np.cos(theta1)
    p2 = n_h * np.cos(theta2)
    p3 = n_l * np.cos(theta3)
    p_s = n_s * np.cos(theta_s)

    # GENERAL MATRIX ELEMENTS (FROM WOLF AND BORN)

    #        M11 = (np.cos(beta2)*np.cos(beta3) - (p3/p2)*np.sin(beta2)*np.sin(beta3))**N
    #        M12 = ((-1/p3) * np.cos(beta2) * np.sin(beta3) - (1/p2) * np.sin(beta2) * np.cos(beta3))**N
    #        M21 = ((-p2 * np.sin(beta2) * np.cos(beta3)) - (p3 * np.cos(beta2)*np.sin(beta3)))**N
    #        M22 = ((np.cos(beta2) * np.cos(beta3)) - (p2/p3)*np.sin(beta2) * np.sin(beta3))**N
    M1 = np.zeros((2, 2), dtype=np.complex)
    M2 = np.zeros((2, 2), dtype=np.complex)

    R = []
    for i in wav_range:
        # CALCULATING BETA FOR LAYERS
        beta2 = (2 * np.pi / i) * (n_h * h_2) * np.cos(theta2)
        beta3 = (2 * np.pi / i) * (n_l * h_3) * np.cos(theta3)

        M1[0, 0] = np.cos(beta2)
        M1[0, 1] = (-1j / p2) * np.sin(beta2)
        M1[1, 0] = (-1j * p2) * np.sin(beta2)
        M1[1, 1] = np.cos(beta2)

        M2[0, 0] = np.cos(beta3)
        M2[0, 1] = (-1j / p3) * np.sin(beta3)
        M2[1, 0] = (-1j * p3) * np.sin(beta3)
        M2[1, 1] = np.cos(beta3)

        M = np.linalg.matrix_power((np.dot(M1, M2)), N)
        # REFLECTION COEFFICIENT
        little_r = (((M[0, 0] + (M[0, 1] * p_s)) * p1) - (M[1, 0] + (M[1, 1] * p_s))) / (((M[0, 0] + (M[0, 1] * p_s)) * p1) + (M[1, 0] + (M[1, 1] * p_s)))
        R.append(np.abs(little_r ** 2))

    # REFLECTIVITY
    return R


prog_run = 1  # Setting for the while loop to run

while (prog_run == 1):  # While loop that runs for the amount of time the user wants it to

    print("Some common materials in Bragg Reflectors")
    print("\n")

    # Displaying a makeshift table of some common Bragg reflector materials for ease of use
    refrac_indices = {
        "Magnesium Fluoride": 1.37,
        "Silicon Dioxide": 1.54,
        "Tantalum Pentoxide": 2.28,
        "Zinc Sulphide": 2.32,
        "Titanium Dioxide": 2.40,
        "Cryolite": 1.35,
        "Glass": 1.50,
    }
    print("Refractive Index                 Material")
    print("\n")
    for key, value in refrac_indices.items():
        print("{}, \t\t\t\t {}".format(value, key))

    # Inputting the general information for the system

    n_hstr = input('Choose a material from above for the higher refractive index material, or enter another refractive index if it is not listed: ')
    if n_hstr in refrac_indices.keys():
        n_hstr = refrac_indices.get(n_hstr)

    n_lstr = input('Choose a material from above for the lower refractive index material, or enter another refractive index if it is not listed: ')
    if n_lstr in refrac_indices.keys():
        n_lstr = refrac_indices.get(n_lstr)

    n_sstry = input('Choose a material from above for the substrate material, or enter another refractive index if it is not listed: ')
    if n_sstry in refrac_indices.keys():
        n_sstry = refrac_indices.get(n_sstry)

    N_str = input('Enter the number of stacks in the reflector: ')
    # wavelength_str = input('What is the wavelength of incident light in metres? To input a wavelength to a particular power, place "e" in place of "x10". For example, 500nm would be input as 500e-9: ')

    # Converting these inputs into appropriate variables
    n_h = np.abs(float(n_hstr))  # Zinc Sulphide       2.3
    n_l = np.abs(float(n_lstr))  # Cryolite            1.35
    n_s = np.abs(float(n_sstry))  # Glass               1.5
    N = np.abs(int(N_str))  # Number of stacks in the Bragg Reflector
    wavelength = 500
    wav_range = np.arange(200, 800)

    # Other Variables
    # N_index = np.arange(0,N,1)
    R = np.zeros(len(wav_range))
    # INDEX METHOD FOR CALCULATING REFLECTIVITY (TEST VALUES)
    for i in range(len(wav_range)):
        R[i] = ((1 - (1 / n_s) * (n_l / n_h) ** (2 * N)) / (1 + (1 / n_s) * (n_l / n_h) ** (2 * N))) ** 2

    # MATRIX METHOD
    # N_matrix = np.arange(0,20,1)
    # R_array = np.zeros(len(wav_range))
    theta_str = input('Enter the angle of incidence in degrees: ')
    theta = int(theta_str)

    R_array = ReflectionCalculatorFunction(n_h, n_l, n_s, N, wavelength, theta, wav_range)

    # Plotting the final reflectivity versus N plot, with formatting for the user
    plt.plot(wav_range, R_array, label='Matrix Method')
    # plt.plot(range(0,N), R, label='Index Method')
    plt.xlabel('N')
    plt.ylabel('Reflectivity')
    plt.legend()
    plt.show()

    run_again = 0
    while run_again != 'y' and run_again != 'n':
        run_again = input('Would you like to run the program again? Y/N: ').lower()
        if run_again == 'y':
            continue
        if run_again == 'n':
            prog_run = 0
        else:
            print("Please enter either Y or N.")
