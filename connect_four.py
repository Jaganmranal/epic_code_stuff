board = []
for i in range (42):
    board.append(0)
player1 = input('Input player 1 username: ')
player2 = input('Input player 2 username: ')
winner = 0
chips = 0

def show(game):
    for i in range(6):
        print(game[35-7*i:42-7*i])
        
def check(game, chips):
      if chips <= 6:
          return False
      else:
          
#horizontal check
          for a in range(24):
                i = a % 6
                j = int((a - i)/6) 
                if board[j+7*i] * board[j+7*i + 1] * board[j+7*i + 2] * board[j+7*i + 3] == 16:
                    winner = 2
                    return True, winner
                elif board[j+ 7*i] * board[j+7*i + 1] * board[j+7*i + 2] * board[j+7*i + 3] == 1:
                    winner = 1
                    return True, winner
            
#vertical check
          for a in range(21):
                i = a % 3
                j = int((a - i)/3)
                if board[j+7*i] * board[j+7*i + 7] * board[j+7*i + 14] * board[j+7*i + 21] == 16:
                    winner = 2
                    return True, winner
                elif board[j+ 7*i] * board[j+7*i + 7] * board[j+7*i + 14] * board[j+7*i + 21] == 1:
                    winner = 1
                    return True, winner
                  
#positive diagonal check
          for a in range(12):
              i = a % 3
              j = int((a - i)/3)
              if board[j + 7*i] * board[j + 1 + 7 * (i + 1)] * board[j + 2 + 7 * (i + 2)] * board[j + 3 + 7 * (i + 3)] == 16:
                    winner = 2
                    return True, winner
              elif board[j + 7*i] * board[j + 1 + 7 * (i + 1)] * board[j + 2 + 7 * (i + 2)] * board[j + 3 + 7 * (i + 3)] == 1:
                    winner = 1
                    return True, winner
                
#negative diagonal check
          for a in range(12):
              i = a % 3
              j = int((a - i)/3 + 3)
              if board[j + 7*i] * board[j - 1 + 7 * (i + 1)] * board[j - 2 + 7 * (i + 2)] * board[j - 3 + 7 * (i + 3)] == 16:
                    winner = 2
                    return True, winner
              elif board[j + 7*i] * board[j - 1 + 7 * (i + 1)] * board[j - 2 + 7 * (i + 2)] * board[j - 3 + 7 * (i + 3)] == 1:
                    winner = 1
                    return True, winner
      return False

while True:
    show(board)
    choice1 = int(input('Player 1: '))
    for i in range(6):
        if board[choice1 + 7*i] == 0:
            board[choice1 + 7*i] = 1
            chips += 1
            break
    if check(board, chips) != 0:
        show(board)
        print("lol, ur kinda trash", player2)
        print(player1, "won")
        winner = 1
        break
    show(board)
    choice2 = int(input('Player 2: '))
    for i in range(6):
        if board[choice2 + 7*i] == 0:
            board[choice2 + 7*i] = 2
            chips += 1
            break
    if check(board, chips) != 0:
        show(board)
        print(player2, "has won, legit cracked")
        print(player1, 'is kinda slackin')
        winner = 2
        break