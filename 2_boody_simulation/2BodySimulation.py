import pygame as pg
import random
import sys

from vec2 import vec2
from VectorGrid import VectorGrid
from Object import Object

class TwoBodySimulation:
  SCREEN_WIDTH  = 512
  SCREEN_HEIGHT = 512
  AMOUNT_OBJS = 2#_500_000
  # first grid (1x1) is always skipped in calculating grid pos
  # but not in updating the objects position
  GRID_DEPTH = 3

  # colors
  WHITE = (255,255,255)
  BLACK = (  0,  0,  0)
  GREY  = ( 30, 30, 30)


  def __init__(self):
    self.obj_arr = []
    self.makeObjects()

  def makeObjects(self):
    for i in range(self.AMOUNT_OBJS):
      rand_x, rand_y = random.randint(0, self.SCREEN_WIDTH), random.randint(0, self.SCREEN_HEIGHT)
      rand_mass = int(random.random() * 10000) / 100
      self.obj_arr.append(Object(vec2(rand_x, rand_y), self.GRID_DEPTH, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT), rand_mass))

  def updateObjPos(self):
    """
    loops through the obj_arr and gets the 
    vectors of all the vector grids then adds
    the object while taking in acount for the obj's wieght 
    """
    pass

  def updateVectorGrid(self):
    # loop inversely through the grid depth
    # get grid wieght for the cell
    # using previous grid depth get the larger grids weight per cell
    # for cell in self.vector_grids[-1]:

    # get the position in the last grid
    for cell in self.vector_grids[-1]:
      cell_center_of_mass = vec2(0,0) # x,y of the averaged mass and position of the objects in the cell
      average_position    = vec2(0,0) # position of all obj's in the cell divide by the amount of objs
      total_positions     = vec2(0,0)
      returning_vector    = vec2(0,0)
      total_obj_mass_in_cell = 0.0
      total_objects_in_cell  = 0

      cell_update_velocity = vec2(0,0) # direction toward the center of mass from the center of the cell
      for obj in self.obj_arr:
        if obj.getGridPosatDepth(-1) == cell:
          total_obj_mass_in_cell += obj.mass
          total_positions        += obj.position
          total_objects_in_cell  += 1
      
      # calculate the averages
      average_position = total_positions / total_objects_in_cell
      
      # using average pos and cell center find the vector toward a centeral point of gravitaion


      cell = returning_vector

  def run(self):
    self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), vsync=1)
    self.clock = pg.time.Clock()
    self.vector_grids = [VectorGrid]
    for grid in range(self.GRID_DEPTH + 1):
      self.vector_grids.append(VectorGrid(2**(grid)))
    # print(self.obj_arr[0].grid_positions)
    for obj in self.obj_arr:
      print(obj)

    while True:
      self.screen.fill(self.GREY)
      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
      self.updateVectorGrid()
      self.updateObjPos()

      for obj in self.obj_arr:
        pg.draw.circle(self.screen, self.WHITE, (obj.position[0], obj.position[1]), 1)
      
      pg.display.flip()
      
      self.clock.tick(60)
      pg.display.set_caption(str(int(self.clock.get_fps() * 100) / 100))

## end TBS

if __name__ == "__main__":
  pg.init()
  TBS = TwoBodySimulation()
  TBS.run()