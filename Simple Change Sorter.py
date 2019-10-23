# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:17:25 2015
EG21007 - Introduction To Programming
Assignment 2: Optimal change
@author: Liam
"""


"""
This program calculates the optimal change return when a user inputs the price
of an item and how much money they have. This program uses dictionaries and floor division
to calculate the optimal change output. This was my first program using dictionaries. 

"""

#Task A. Gathering inputs and calculating change due

#Getting user inputs
_itemprice = float(input("Please enter the price of the item: £"))
_usercash =  float(input("Please enter how much money you have: £"))
print(" ")

#calculating change due
change = _usercash - _itemprice

#Verifying the user has enough cash to complete the transaction
if _itemprice > _usercash:
    print("Insufficient funds.")
elif _itemprice == _usercash:
    print("No change is needed to be given.")
else:
    print("Your item price is {:.2f}, you have given {:.2f}, therefore your change is {:.2f}".format(_itemprice,_usercash, change))
    
#Setting up a dictionary with all the potential amounts of change    
_availablechange ={50.00:'£50',20.00:'£20',10.00:'£10',5.00:'£5',2.00:'£2',1.00:'£1',0.50:'50p',0.20:'20p',0.10:'10p',0.05:'5p',0.02:'2p',0.01:'1p'}

print("")
print("Change Due: £{:.2f}".format(change))
print("Please return: ", end = " ")

#looping over each potential denomination. Dictionary is sorted from highest denomination to lowest
#checking how many times a currency value goes into the change, and then returning how many notes/coins are needed per value.
for key, value in sorted(_availablechange.items(), reverse = True): 
    if change >= key:
        x = change//key
        change = change - key*x
        print("{:.0f}x{:.3s}".format(x,value), end = " ")

