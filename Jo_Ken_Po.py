# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:32:09 2020

@author: Rogerio
"""

from random import randint
import time

choose = {0:"Paper",1:"Rock",2:"Scissors"} # Choices to play.
computer = 0
player = 0
print('*'*20)
print('JO KEN PO')
print('*'*20)

# It presents the options to the player and asks his input.
while True:
   for c in choose:
       print(f"{c} - {choose[c]}")
   player = input('Make your choice:')
#Validate the input
   if player == '0' or player == '1' or player == '2':
       break
   else:
        print('Wrong answer, please try again!')

             
computer = randint(0,2) #Computer make his choice.

player = int(player)

print(end='\n')
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(1)
print(end='\n')

#Possible results.
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
       print('You won! DAMN IT!')
elif player == computer:
       print('Draw')
else:
       print('I won!!! LOOOSER!!!!')
print(end='\n')

#Show chose options.      
print(f"You played {choose[player]} and I played {choose[computer]}")
