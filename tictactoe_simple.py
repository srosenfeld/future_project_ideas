import numpy as np

count = 1
lastpicked = "O"

board = [
    
["_","_","_"],
["_","_","_"],
["_","_","_"]

    ]


def printboard ():
    print("Turn " + str(count))
    print(np.matrix(board))


def choice(a,x,y):
    board[x][y] = a

    
while True:
    printboard()
    x = int(input("Which row?")) - 1
    y = int(input("Which column?")) - 1
    a = input("X or O ?")
    choice(a,x,y)
    
