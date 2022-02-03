from board import Board
import random

class Game:
  def __init__(self) -> None:
      self.board = Board()
      self.remaining_pos = self.getPositions()
      self.current_player = 'O'
      self.game_over = False

  def getPositions(self):
    positions = []
    grid = self.board.grid
    for row in range(len(grid)):
      for col in range(len(grid)):
        positions.append([row, col])
    return positions

  def switchPlayer(self):
    self.current_player = 'X' if self.current_player is 'O' else 'O'

  def playTurn(self):
    pos = random.sample(self.remaining_pos,1)[0]
    self.board.placeMarker(pos, self.current_player)
    self.board.printBoard()
  
  def newRound(self):
    if self.board.win(self.current_player):
      print(f'{self.current_player}\'s won!')
      self.game_over = True
    elif len(self.remaining_pos) == 0:
      print(f'Game over - cat\'s game!')
    else:
      self.switchPlayer()

  def playGame(self):
    self.board.printBoard()
    while not self.game_over:
      self.playTurn()
      self.newRound()

game = Game()
game.playGame()