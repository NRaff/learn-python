from board import Board
import random

class Game:
  def __init__(self) -> None:
      self.board = Board()
      self.remaining_pos = self.getPositions()
      self.current_player = 'O'

  def getPositions(self):
    positions = []
    grid = self.board.grid
    for row in range(len(grid)):
      for col in range(len(grid)):
        positions.append([row, col])
    return positions

  def switchPlayer(self):
    self.current_player = 'X' if self.current_player is 'O' else 'O'

game = Game()
print(game.remaining_pos)