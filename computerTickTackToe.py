import random

PLAYERS = ('X', 'O')
# Create the board
def createBoard(size=3):
  # do things to create the board
  return [['_'] * size for i in range(size)]

# Set the player
def switchPlayers(player_idx=0):
  return PLAYERS[player_idx + 1] if player_idx == 0 else PLAYERS[player_idx - 1]
  # set the other player to active

def generatePositions(board):
  # return all possible positions to choose from
  positions = []
  for row in range(len(board)):
    for col in range(len(board)):
      positions.append([row, col])
  return positions

# get new position
def getPosition(positions):
  pos = random.sample(positions, 1)[0]
  positions.remove(pos)
  return pos

# Play piece
def playPiece(board, player, pos):
  row = pos[0]
  col = pos[1]
  board[row][col] = player

# print board
def printBoard(board):
  s = ' '
  for row in board:
    print(s.join(row))
  print()

# check for win (horizontal, vertical, diagonal)
def win(board, player):
  return winH(board, player) or winV(board, player) or winD(board,player)

def winH(board, player):
  for row in board:
    expectWin = True
    for item in row:
      if item is not player:
        expectWin = False
        break
    if expectWin:
      return True
  return False

def winV(board, player):
  for col in range(len(board)):
    expectWin = True
    for row in range(len(board)):
      if board[row][col] is not player:
        expectWin = False
        break
    if expectWin:
      return True
  return False

def winD(board, player):
  return winDownRight(board, player) or winDownLeft(board, player)

def winDownRight(board, player):
  for place in range(len(board)):
    if board[place][place] is not player:
      return False
  return True

def winDownLeft(board, player):
  for place in range(len(board)):
    row = place
    col = -(place+1)
    if board[row][col] is not player:
      return False
  return True

def playGame(size=3):
  board = createBoard(size)
  positions = generatePositions(board)
  printBoard(board)
  player = switchPlayers()
  gameOver = False
  winMsg = ''
  while not gameOver:
    pos = getPosition(positions)
    playPiece(board, player, pos)
    printBoard(board)
    if win(board, player):
      gameOver = True
      winMsg = f'Game over, {player}\'s won!'
      break
    elif len(positions) == 0:
      gameOver = True
      winMsg = f'Game over, cat\'s game!'
      break
    else:
      player = switchPlayers(PLAYERS.index(player))
  return winMsg
  


print(playGame(3))