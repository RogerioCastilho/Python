# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 00:37:48 2020

@author: Rogerio
"""
# Choises.
theBoard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}
# Backup choices if reset game after the end.
reset_board = []

for key in theBoard:
    reset_board.append(key)

# Board shown in every movement.    
def board(b):
    print(b['7']+"|"+b['8']+"|"+b['9'])
    print("-|-|-")
    print(b['4']+"|"+b['5']+"|"+b['6'])
    print("-|-|-")
    print(b['1']+"|"+b['2']+"|"+b['3'])
    
# Here where game begins.
def game():
    
    turn ='X'
    count = 0
    print('-'*13)
    print('|TIC-TAC-TOE|')
    print('-'*13)
    print(''' To play the game use only numbers from 1 up to 9. 
 The numbering is arranged as follows.\n
          7|8|9
          -|-|-
          4|5|6
          -|-|-
          1|2|3''')
    # Ask for input, check the conditions and record the turn movement.
    while True:
        board(theBoard)
        move = input(f"It's your turn {turn}. Move to which place?")
        print('\n')
        if move in theBoard.keys() and theBoard[move] == " ":
            theBoard[move] = turn
            count +=1
            
        elif move not in theBoard.keys():
            print("The number is out of range")
            continue
        else:
            print("You typed a filled space, please try again")
            continue
        # Check conditional to win.
        if count >=5:
        # Check who wins horizontal.
            if theBoard['7'] == theBoard['8'] == theBoard['9'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            
            #Check who wins vertical.
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            
            #Check who wins diagonal.  
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] !=' ':
                board(theBoard)
                print(f"Player {turn} won!")
                break
            # Draw!
            if count == 9:
                board(theBoard)
                print('DRAW!')
                break
        # Change the turn player.    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    # Do you want ot play again?        
    while True:
        reset = str(input("Do you want to play again?(y/n)")).lower().strip()
        if reset == 'y' or reset == 'n':
            break
        else:
            print("Wrong answer. Please choose 'y' for yes or 'n' for no.")  
    if reset == 'y':
        for key in reset_board:
            theBoard[key] = " " # Reset theBoard variable.
        game() # Start game again.
    else:
        print('See you next time!')
game() #Start the game for the first time.