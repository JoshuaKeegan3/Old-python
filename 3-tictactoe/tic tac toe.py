#tic tac toe
board = [1,2,3,4,5,6,7,8,9]
display_board = []
player = 0
playernames =[]
move = 0
for i in range (1,3):
    playernames.append(input('Player {}, What is your name?'.format(i)).title())
for i in range(0,9):
      if (i+1)%3 != 0:
          display_board.append(str (board[i]))
          display_board.append('|')
      else:
          display_board.append(str (board[i]))
          display_board.append('\n------\n')
print(''.join(display_board))
player1win = False
player2win = False
move = 'not in board'
while not player1win and not player2win:
    while move not in board:
        try:
            move = int(input('{}! Pick a square'.format(playernames[player%2])))
        except:
            print('enter a number on the board')
    if player %2 == 0:
        board[move-1] = 'O'
    elif player %2 == 1:
        board[move-1] = 'X'
    
    player += 1
    display_board.clear()
    for i in range(0,9):
        if (i+1)%3 != 0:
            display_board.append(str (board[i]))
            display_board.append('|')
        else:
            display_board.append(str (board[i]))
            display_board.append('\n------\n')
    print(''.join(display_board))
    for x in range (0,3):
        player1win = (board[4] == 'O' and ((board[0] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[6] == 'O')) or (board[x] == 'O' and board[x+3] == 'O' and board[x+6] == 'O') or (board[x*3] == 'O' and board[x*3+1] == 'O' and board[x*3+2]== 'O')) 
        player2win = (board[4] == 'X' and ((board[0] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[6] == 'X')) or (board[x] == 'X' and board[x+3] == 'X' and board[x+6] == 'X') or (board[x*3] == 'X' and board[x*3+1] == 'X' and board[x*3+2]== 'X'))
        if player1win or player2win:
            break
    if player == 9:
        break
if player1win:
    print('{} wins!'.format(playernames[0]))
elif player2win:
    print('{} wins!'.format(playernames[1]))
else:
    print('tie')
