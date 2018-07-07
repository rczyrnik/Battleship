import random
import os

print("Welcome to the Plot of Land that will someday maybe be a Battleship Program")


# Let's make two random boards
# No one gets to place their own ships. That's commie talk.

def MakeBoard(n):
    return
# Nevermind. Lets not do that.

def DisplayBoard(Board):
    os.system('clear')

    print()

    print("Here's your board")
    
    print()
    
    print("   _____ _____ _____ _____")   # top bar
    
    c = 1
    for n in Board:
        print("  |{0:2}   |{1:2}   |{2:2}   |{3:2}   |".format(c, c+1, c+2, c+3))   # for each row of the board
        print("  |", end='')
        for m in n:
            if m == 0:
                print("     ", end='|')
            if m == 1:
                print("  O  ", end='|')
            if m == 2:
                print("  X  ", end='|')
            if m == 3:
                print("  x  ", end='|')
        print("\n  |_____|_____|_____|_____|")   # for each row of the board
        c += 4
    print()
    print()




    return



if __name__ == "__main__":

    #board = [[0]*height]*height
    #board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #board = [[0,0,0],[0,0,0],[0,0,0]]

    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    board = [[2,0,3,0],[0,0,3,0],[0,0,3,0],[1,0,0,0]]


    


#    size = 2
#    Place(size, board)
    DisplayBoard(board)
#    player = 1
#    Turn(board, player)
#    DisplayBoard(board)


#
#def Place(size, board):
#    choice = random.randint(0, 1)
#    if choice == 0:         # vertical ships
#        row = random.randint(0, len(board)-size-1)
#        col = random.randint(0, len(board)-1)
#        n = 0
#        while n<=size-1:
#            board[row+n][col]=1
#            n +=1
#    else:                   # horizontal ships
#        row = random.randint(0, len(board)-1)
#        col = random.randint(0, len(board)-size-1)
#        n = 0
#        while n<=size-1:
#            board[row][col+n]=1
#            n +=1
#    return board
#
#def Check(board, row, col):
#    if board[row][col]==1:
#       print("It's a hit!")
#       board[row][col] = 2
#       hitormiss = "H"
#    else:
#        print("It's a miss!")
#        board[row][col] = 3
#        hitormiss = "M"
#    return board, hitormiss
#
#def Turn(board, player):
#    if player == 1:
#        row = random.randint(0, len(board)-1)
#        col = random.randint(0, len(board)-1)
#        board, hitormiss = Check(board, row, col)
#        if hitormiss == "H":
#            whichway = random.randint(1, 4)
#            if whichway == 1:
#                board, hitormiss = Check(board, row-1, col)
#            if whichway == 2:
#                board, hitormiss = Check(board, row, col+1)
#            if whichway == 3:
#                board, hitormiss = Check(board, row+1, col)
#            if whichway == 4:
#                board, hitormiss = Check(board, row, col-1)
#        if hitormiss == "M":
#            player = 0
#
#
#    return board
