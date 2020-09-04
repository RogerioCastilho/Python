# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:32:09 2020

@author: Rogerio
"""

from random import randint
import time

choose = {0:"Paper",1:"Rock",2:"Scissors"}
condition = True
computer = 0

print('*'*20)
print('JO KEN PO')
print('*'*20)


while condition == True:
    for c in choose:
        print(f"{c} - {choose[c]}")
    player = input('Make your choice:')

    if player == '0' or player == '1' or player == '2':
        condition = False
    else:
        print('Wrong answer, please try again!')
              
computer = randint(0,2)
player = int(player)
print(end='\n')
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(1)
print(end='\n')
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 1):
       print('You won! DAMN IT!')
elif player == computer:
       print('Draw')
else:
       print('I won!!! LOOOSER!!!!')
print(end='\n')      
print(f"You played {choose[player]} and I played {choose[computer]}")
