def check_rows(symbol):
    for r in range(3):
        count=0;
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,"won")
            return True
    return False

def check_cols(symbol):
    for r in range(3):
        count=0;
        for c in range(3):
            if board[c][r]==symbol:
                count+=1
        if count==3:
            print(symbol,"won")
            return True
    return False

def check_diagonals(symbol):
    count=0
    for r in range(3):
        if board[r][r]==symbol:
            count+=1
    if count==3:
        print(symbol,"won")
        return True
    count=0
    for r in range(3):
        if board[r][2-r]==symbol:
            count+=1
    if count==3:
        print(symbol,"won")
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row - 1/2/3 : "))
        col=int(input("Enter column - 1/2/3 : "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break;
        else:
            print("Invalid input. Please enter again.")
    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn : ")
            #p1=input()
            place(p1)
            if won(p1):
                break
        else:
            print("O turn : ")
            #p2=input()
            place(p2)
            if won(p2):
                break
    if not(won(p1)) and not(won(p2)):
        print("Draw")

import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='X'
p2='O'
play()