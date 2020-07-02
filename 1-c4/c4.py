#connect 4 7x7
rows = 7
colummns = 7

import turtle
turtle = turtle.Turtle()
turtle.speed(10)
turtle.penup()
turtle.goto(-300,-320)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('yellow')
for i in range(4):
    turtle.forward(630)
    turtle.left(90)
turtle.end_fill()

turtle.shape('circle')
turtle.shapesize(3)#80 diameter
turtle.penup()
turtle.color('white')


for y in range (7):
    turtle.goto(-260,-280 + y* 90)
    turtle.stamp()
    for x in range(7):
        turtle.forward(90)
        turtle.stamp()

    
board = {1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
player1 = input('Player One what is your name').title()
player2 = input('Player Two what is your name').title()
for row in range(1,8):
    for column in range(7):
        board[row].append('clear')
turn=1
player1win = False
player2win = False
spaces = True
while not player1win and not player2win:
    spaces = True
    if turn > 0:
        while spaces:
            try:
                move = int(input('{} pick a column'.format(player1)))
            
                for key in range(1,8):
                    if move == key:
                        for row in range(7):
                            if board[key][row] == 'clear':
                                board[key][row] = 'red'
                                turtle.color('red')
                                -260,-280
                                turtle.goto(-260 + (key-1)*90, -280 + row*90)
                                turtle.stamp()
                                spaces = False
                                break
                            if row == 6:
                                print('that column is full')
            except:
                print('Enter a number from 1-7 eg: 6')
    else:
        while spaces:
            try:
                move = int(input('{} pick a column'.format(player2)))
            
                for key in range(1,8):
                    if move == key:
                        for row in range(7):
                            if board[key][row] == 'clear':
                                board[key][row] = 'blue'
                                turtle.color('blue')
                                turtle.goto(-260 + (key-1)*90, -280 + row*90)
                                turtle.stamp()
                                spaces = False
                                break
                            if row == 6:
                                    print('that column is full')
            except:
                print('Enter a number from 1-7 eg: 6')
    turn *= -1

    #vertical win
    for row in range (1,7):
        for column in range (0,4):
            if board[row][column] == board[row][column+1] == board[row][column+2] == board[row][column+3]:
                if board[row][column] == 'red':
                    player1win = True
                elif board[row][column] =='blue':
                    player2win = True

    #horrosontal    
    for row in range (1,5):
        for column in range (0,7):
            if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row+3][column]:
                if board[row][column] == 'red':
                    player1win = True
                elif board[row][column] =='blue':
                    player2win = True
    #diagonal right
    for column in range (1,5):
        for row in range (0,4):
            if board[column][row] == board[column+1][row+1] == board[column+2][row + 2] == board[column + 3][row +3]:
                if board[column][row] == 'red':
                    player1win = True
                elif board[column][row] =='blue':
                    player2win = True
    #diagonal left               
    for column in range (4,8):
        for row in range (0,4):
            if board[column][row] == board[column-1][row+1] == board[column-2][row + 2] == board[column - 3][row +3]:
                if board[column][row] == 'red':
                    player1win = True
                elif board[column][row] =='blue':
                    player2win = True

    
if player1win:
    print('{} wins!'.format(player1))
else:
    print('{} wins!'.format(player2))

            
    

