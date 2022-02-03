class Board:
  def __init__(self, size=3):
      """
      Constructs a new board object
      """
      self.grid = self.createBoard(size)
      self.remaining_pos = self.getPositions()
  
  def createBoard(self, size):
    return [['_'] * size for i in range(size)]
  
  def printBoard(self):
    for row in self.grid:
      s = ' '
      print(s.join(row))
    print()

  def getPositions(self):
    positions = []
    for row in range(len(self.grid)):
      for col in range(len(self.grid)):
        positions.append([row, col])
    return positions
  
  def grid(self):
    return self.grid

  def remaining_pos(self):
    return self.remaining_pos

  def placeMarker(self, pos, marker):
    row = pos[0]
    col = pos[1]
    self.grid[row][col] = marker