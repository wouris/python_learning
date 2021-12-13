import os
import time
import random

def clrscr():   #clearing the screen
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]
player_symbol = 'X'
AI_symbol = 'O'

def checkwinner(turn,symbol):
    
    for row in range(0,2+1):  #checking rows
        if board[row].count(symbol) == 3:
            isWinner = True
            break
        else:
            isWinner = False
            
    if isWinner == False:
        for col in range(0,2+1): #checking columns
            num = 0
            for row in range(0,2+1):
                if board[row][col] == symbol:
                    num += 1
            if num == 3:
                isWinner = True
    
    if isWinner == False:
        i = 0
        num = 0
        for col in range(0, 2+1): #checking diagonal
            """
            \
            """
            row = i
            if board[row][col] == symbol:
                num += 1
            i += 1
            if num == 3:
                isWinner = True
    
    if isWinner == False:
        num = 0
        i = 2
        for col in range(0, 2+1): #checking diagonal
            """
            /
            """
            row = i
            if board[row][col] == symbol:
                num += 1
            i -= 1
            if num == 3:
                isWinner = True
            
    if isWinner == True:
        clrscr()
        print_board()
        if turn == 'player':
            print('You win!')
        else:
            print('You lose!')
        exit()

def print_board():
    print(board[0][0],board[0][1],board[0][2] + '\n' +
          board[1][0],board[1][1],board[1][2] + '\n' +
          board[2][0],board[2][1],board[2][2]
          )


while True:
    clrscr()
    print_board()
    print(board[0].count('X'))
    userinput = input('Your input: ')
    
    if userinput == 'x':
        break
    else:
        pass
    
    for i in userinput:
        if i == 'A':
            row = 0
        elif i == 'B':
            row = 1
        elif i == 'C':
            row = 2
        
        if i == '1':
            col = 0
        elif i == '2':
            col = 1
        elif i == '3':
            col = 2
    
    try:
        board[row][col]
    except:
        print('Invalid input.')
        time.sleep(2)
        continue
    
    if board[row][col] == '-':
            board[row][col] = player_symbol
    else:
        print('Position is occupied.')
        time.sleep(2)
        continue
    
    checkwinner('player',player_symbol)
    
    while True:
        randomrow = ['A','B','C']
        randomcol = ['1','2','3']
        
        randrow = random.choice(randomrow)
        randcol = random.choice(randomcol)
        AI_choice = randrow + randcol
        
        for i in AI_choice:
            if i == 'A':
                randrow = 0
            elif i == 'B':
                randrow = 1
            elif i == 'C':
                randrow = 2
            
            if i == '1':
                randcol = 0
            elif i == '2':
                randcol = 1
            elif i == '3':
                randcol = 2
        
        if board[randrow][randcol] == '-':
            board[randrow][randcol] = AI_symbol
            break
    checkwinner('AI',AI_symbol)