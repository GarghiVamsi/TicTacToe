#defining TicTacToe board
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',6: ' ',7: ' ',8: ' ',9: ' ' }

#printing board 
def myBoard(board): #Metod to print the board into the screen and display its content
    print(board[1]+ '|' + board[2]+ '|' + board[3])
    print ('-+-+-')
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print ('-+-+-')
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print ("\n") # This prints new line

myBoard(board)

def freeSpace (position):    #Method to define if a space is free or not so the algorithm can pick the space that is free
    if(board[position]== ' '):
        return True
    else:
        return False

def checkDraw ():
    for value in board.values():
        if board[value] == ' ':
            return False

    return True

def checkWin ():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def main(letter,position):
    if freeSpace(position):
        board[position] = letter
        myBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if (checkWin()):
            if letter == 'X':
                print("bot wins!")
                exit ()
            else:
                letter == 'O'
                print ("player wins!")
                exit ()

    else:
        print ("can't insert, value already there ")
        position = int(input("enter new position: "))
        main(letter,position)
        return

player = 'O'
comp = 'X'

def forPlayerMove():
    position = int(input("enter position for 'O'"))
    main(player,position)
    return

def forComputerMove ():
    position = int(input("enter position for 'X'"))
    main(comp,position)
    return

while not checkWin():
    forComputerMove()
    forPlayerMove()
