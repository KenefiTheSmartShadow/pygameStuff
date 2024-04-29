import pygame as pg
import numpy as np
import sys

class vec2:
  def __init__(self, x : float, y : float):
    self.x_vector = x # vertical
    self.y_vector = y # horizontal

  # TODO Add dot product, cross product, division, check __mul__()
  def __add__(self, other) -> vec2:
    return vec2(self.x_vector + other.x_vector, self.y_vector + other.y_vector)
  def __sub__(self, other) -> vec2:
    return vec2(self.x_vector - other.x_vector, self.y_vector - other.y_vector)
  def __mul__(self, other) -> vec2:
    return vec2(self.x_vector * other.x_vector, self.y_vector * other.y_vector)
## end vec2

class VectorGrid:
  def __init__(self):
    pass

  def setGridWeights(self):
    # make a
    pass

  def getVectors(self, grid_depth, grid_index) -> vec2:
    """
    grid_depth is the amount of grids\n
    grid_index is the pos of the grid in the grid_depth grid\n
    Returns a vec2\n
    """
    # get the grid weight convert to a vector and return as vec2
    grid_x_vector = self.getGridXVector(grid_depth, grid_index)
    grid_y_vector = self.getGridYVector(grid_depth, grid_index)
    local_grid_vector = vec2(grid_x_vector, grid_y_vector)
    pass

  def getGridXVector(self, grid_depth, grid_index) -> float:
    # get the amount of object in the grid
    # average the x positions
    # convert to float
    pass
  def getGridYVector(self, grid_depth, grid_index) -> float:
    pass
## end VectorGrid

class Object:
  # pos as (x, y)
  # (0,0) | (1,0)
  # -------------
  # (0,1) | (1,1)
  grid_positions = []

  def __init__(self, position : vec2, grid_amount, window_size) -> None:
    self.position = position
    self.W_SIZE = window_size
    self.GRID_AMOUNT = grid_amount
    self.getGridPos()

  def getGridPos(self):
    for grid_size in range(self.GRID_AMOUNT):
      grid_width = self.W_SIZE[0] / 2**grid_size
      grid_height = self.W_SIZE[1] / 2**grid_size
      grid_x = int(self.position[0] / grid_width)
      grid_y = int(self.position[1] / grid_height)
      self.grid_positions.append((grid_x, grid_y))

  def updatePos(self, vector_grid : VectorGrid):
    # using grid_pos update the velocity of the object
    pass
## end Object

class TwoodySimulation:
  SCREEN_WIDTH  = 800
  SCREEN_HEIGHT = 600
  AMOUNT_OBJS = 200
  GRID_DEPTH = 3

  # colors
  WHITE = (255, 255, 255)
  BLACK = (  0,   0,   0)

  def __init__(self):
    pass

  def update_pos(self, obj : Object):
    pass

  def run(self):
    pg.init()

    self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), vsync=1)
    self.screen.fill(self.WHITE)

    while True:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
    pass

## end TBS

if __name__ == "__main__":
  pass