# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:48:59 2015
EG21007 - Introduction To Programming
Assignment 3: Game Of Hangman
@author: Liam Winton
"""

"""
This program is a simple game of hangman using Python dictionaries.
A local dictionary is opened and a random word with more than 4 letters is chosen
as the secret word. 
The random word is broken into a list of characters and stored in a list.
The user guesses a letter and the list is checked for that letter. 
If the guess is wrong, the letter is added to a "blacklist" and the user is not allowed to guess again.
The user has (length of the secret word) * 2 guesses. 
If the user guesses correctly the secret word is displayed with the correctly guessed characters in the correct location.
Once the user guesses the secret word the game ends. 
If the user does not win then the secret word is displayed and the game ends. 

The difficult level can be adjusted by adjusting the number of guesses the user gets on line 47.

"""



import random

def loc_letter(letter,word):
 return [i for (i,v) in enumerate(word) if v == letter] #Code given to determine location of letters within a list



#Generating a random word suitable for gameplay
wordslist = []

with open('words.txt','r') as fullwords:
    for line in fullwords:
       if len(line)>=4 or line.isalpha() == True:
            wordslist.append(line.split())      #only accepting words into the potential list with > 4 character and no non letter characters
    
rndword = random.choice(wordslist)   #generating a random word

secretword = list(' '.join(rndword)) #converting the random word into a list of characters
completeword = list('-'*len(secretword))    #a list for holding correctly guessed letters as well as the final result
blacklist = []  #list for holding incorrect guesses


tries = len(secretword)*2   #deciding the number of failed attempts the user is allowed

#Initial screen
print("Secret word is: ",'-'*len(secretword))
print("You have {} attempts to find it".format(tries))
print("Good luck!")


#Gathering and checking use input against secret word
while tries >= 0:
    
    guess = input("Guess a letter: ").lower()       #getting user guess
    
    #formatting output for correct guess
    if guess in secretword:
        for i in loc_letter(guess,secretword):
                completeword[i] = guess
        print('Letter "{}" appears {} times in the secret word'.format(guess, len(loc_letter(guess,secretword)))) 
        print("Guessed: {} ".format(''.join(completeword)))
        print("Missed: {}".format(''.join(blacklist)))
        
    #formatting output for incorrect guess
    if guess in blacklist:     
        print("You have already guessed this incorrect letter, please try again.")
        
    if guess not in secretword and guess not in blacklist:
        blacklist.append(guess)
        print('Letter "{}" does not appear in the secret word.'.format(guess))
        print("You've used one attempt! You have {} attempts left.".format(tries))      
        print("Guessed: {} ".format(''.join(completeword)))
        print("Missed: {}".format(' '.join(blacklist)))
        tries = tries -1
        
    if completeword == secretword:
        tries = 0
        print("Congratulations! You won!")
        break
if completeword != secretword:    
    print("Sorry, you lost! The secret word is '{}'".format(''.join(secretword)))