from vec2 import vec2
import numpy as np

class Object:
  # pos as (x, y)
  # (0,0) | (1,0)
  # -------------
  # (0,1) | (1,1)
  # pos in each consecutive grid layer
  grid_positions = []
  velocity = (0,0)

  def __init__(self, position : vec2, grid_amount, window_size) -> None:
    self.position = position
    self.W_SIZE = window_size
    self.GRID_AMOUNT = grid_amount
    self.getGridPos()

  def getGridPos(self):
    for grid in range(self.GRID_AMOUNT):
      grid_width = self.W_SIZE[0] / 2**(grid + 1)
      grid_height = self.W_SIZE[1] / 2**(grid + 1)
      grid_x = int(self.position[0] / grid_width + 0.5)
      grid_y = int(self.position[1] / grid_height + 0.5)
      self.grid_positions.append(vec2(grid_x, grid_y))
      print(grid_width, grid_height, grid_x, grid_y, self.position)
## end Object