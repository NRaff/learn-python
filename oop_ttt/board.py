class Board:
  def __init__(self, size=3):
      """
      Constructs a new board object
      """
      self.grid = self.createBoard(size)
  
  def createBoard(self, size):
    return [['_'] * size for i in range(size)]
  
  def printBoard(self):
    for row in self.grid:
      s = ' '
      print(s.join(row))
    print()

  def placeMarker(self, pos, marker):
    row = pos[0]
    col = pos[1]
    self.grid[row][col] = marker

  def win(self, marker):
    return self.winHorizontal(marker) or self.winDiagonal(marker) or self.winVertical(marker)

  def winHorizontal(self, marker):
    for row in self.grid:
      didWin = True
      for mark in row:
        if mark is not marker:
          didWin = False
          break
      if didWin: 
        return True
    return False

  def winVertical(self, marker):
    for col in range(len(self.grid)):
      didWin = True
      for row in range(len(self.grid)):
        if self.grid[row][col] is not marker:
          didWin = False
          break
      if didWin:
        return True
    return False

  def winDiagonal(self, marker):
    return self.winDownRight(marker) or self.winDownLeft(marker)

  def winDownRight(self, marker):
    for i in range(len(self.grid)):
      if self.grid[i][i] is not marker:
        return False
    return True

  def winDownLeft(self, marker):
    for i in range(len(self.grid)):
      row = i
      col = -(i + 1)
      if self.grid[row][col] is not marker:
        return False
    return True