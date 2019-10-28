# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Richard Rios, Nic Doorlay
# Instructor: S. Einakian 
# Section: 6
# Functions definitions comes here

def Welcome(): 
    print("Welcome to Tic-Tac-Toe.\nYour goal is to get 3 in a row.\nyou will either pick X or O. X will go first.")
    players = int(input("Do you wish to play against a (1)computer, or with (2)Players? "))
    return players
   
 
def createBoard():
    board = []
    for i in range (9):
        board.append(i+1)
    return board
  
   
# Function needs to be redone using a for-loop according to instructions
def printBoard(list):
    print("",list[0],"|",list[1],"|",list[2])
    print("------------")
    print("",list[3],"|",list[4],"|",list[5])
    print("------------")
    print("",list[6],"|",list[7],"|",list[8])    

   
def pickLetter():
    letter = input("Choose X or O: ")
    while True:    
       if letter == "X" or letter == "O":
           break
       else:
           letter = input("Re-enter X or O: ")
    return letter


def getInput(letter, board):
    while True:
        location = int(input("Where would you like to place your letter (pick in range of 1-9): ")) - 1
        if (location < 0 or location > 8) or board[location] != "" :
            print("Invalid move! Location is already taken. Please try again.")
        else: 
            break
    board.pop(location)
    board.insert(location, letter)
    return board    
   
def checkRows(board):
    if board[0] == board[1] == board[2] and board[0] != "":
        return True, board[0]
    elif board[3] == board[4] == board[5] and board[3] != "":
        return True, board[3]
    elif board[6] == board[7] == board[8] and board[6] != "":
        return True, board[6]
    else:
        return False, board[0]   
   
def checkCols(board):
    if board[0] == board[3] == board[6] and board[0] != "":
        return True, board[0]
    elif board[1] == board[4] == board[7] and board[1] != "":
        return True, board[1]
    elif board[2] == board[5] == board[8] and board[2] != "":
        return True, board[2]
    else:
        return False, board[0]

def checkDiags(board):
    if board[0] == board[4] == board[8] and board[0] != "":
        return True, board[0]
    elif board[2] == board[4] == board[6] and board[2] != "":
        return True, board[2]
    else: 
        return False, board[0]
  
# Function is dependant on the fact that empty squares are represented with
# a "" in the list. Are they? Who knows
def boardFull(board):
    boardNotFull = False
    for square in board:
        if square == "":
            boardNotFull = True
            break
    if boardNotFull != True:
        return True
    else:
        return False

   
def checkWin(board):
    if (checkRows(board))[0] == True:
        winner = checkRows(board)
        print("Congratulations, {}'s won!".format(winner[1]))
    elif (checkCols(board))[0] == True:
        winner = checkCols(board)
        print("Congratulations, {}'s won!".format(winner[1]))
    elif (checkDiags(board))[0] == True:
        winner = checkDiags(board)
        print("Congratulations, {}'s won!".format(winner[1]))
    elif boardFull(board) == True:
        print("It's a draw!")
 
def turnCount(count):
    count += 1
    return count
