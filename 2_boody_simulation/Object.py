from vec2 import vec2
import numpy as np

class Object:
  # pos as (x, y)
  # (0,0) | (1,0)
  # -------------
  # (0,1) | (1,1)
  # pos in each consecutive grid layer
  # saved as a vec2
  W_SIZE = None

  def __init__(self, position : vec2, grid_amount, window_size, mass=1.0) -> None:
    self.grid_positions = []
    self.mass = mass
    self.velocity = (0,0)
    Object.W_SIZE = window_size
    self.position = position
    self.GRID_AMOUNT = grid_amount
    self.getGridPos()

  def getGridPosatDepth(self, depth : int) -> vec2:
    return self.grid_positions[depth]

  def getGridPos(self):
    self.grid_positions.append(vec2(0,0))
    for grid in range(self.GRID_AMOUNT):
      # get half of the window size for a nXn grid
      grid_width = self.W_SIZE[0] / 2 ** (grid + 1) # using powers to get a recursive grid
      grid_x_pos = (int(np.floor(self.position[0] / grid_width)))

      grid_height = self.W_SIZE[1] / 2 ** (grid + 1)
      grid_y_pos = (int(np.floor(self.position[1] / grid_height)))

      self.grid_positions.append(vec2(grid_x_pos, grid_y_pos))

  def __str__(self) -> str:
    sent_str = "Grid Pos': "
    for pos in range(len(self.grid_positions)):
      sent_str += (str(self.grid_positions[pos]) + " ")
    sent_str += ("\n" + "Position: " + str(self.position) + "\n")
    return sent_str
## end Object

if __name__ == "__name__":
  obj = Object(vec2(30, 90), 3, (1024, 1024))
  print(obj)