import pygame as pg
import random
import sys

from vec2 import vec2
from VectorGrid import VectorGrid
from Object import Object

class TwoBodySimulation:
  SCREEN_WIDTH  = 512
  SCREEN_HEIGHT = 512
  AMOUNT_OBJS = 1
  # first grid (1x1) is always skipped in calculating grid pos
  GRID_DEPTH = 3

  # colors
  WHITE = (255,255,255)
  BLACK = (  0,  0,  0)
  GREY  = ( 30, 30, 30)
  # grid colors
  GRID_COLORS = [(0,0,0)]

  obj_arr = []

  def __init__(self):
    self.makeObjects()

  def makeObjects(self):
    for i in range(self.AMOUNT_OBJS):
      rand_x, rand_y = random.randint(0, self.SCREEN_WIDTH), random.randint(0, self.SCREEN_HEIGHT)
      self.obj_arr.append(Object(vec2(rand_x, rand_y), self.GRID_DEPTH, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)))

  def update_pos(self, obj : Object):
    pass

  def createGridColors(self):
    for grid_size in range(self.GRID_DEPTH + 1):
      self.GRID_COLORS.append((20 * grid_size, 20 * grid_size, 20 * grid_size))

  def showGrid(self):
    for depth in range(self.GRID_DEPTH, -1, -1):
      step = int(self.SCREEN_WIDTH / 2**depth)
      color = self.GRID_COLORS[depth]  # Select color based on grid depth, assuming GRID_COLORS has enough entries

      # Draw vertical lines for this depth
      for x in range(step, self.SCREEN_WIDTH, step):
        pg.draw.line(self.screen, color, (x, 0), (x, self.SCREEN_HEIGHT))

      # Draw horizontal lines for this depth
      for y in range(step, self.SCREEN_HEIGHT, step):
        pg.draw.line(self.screen, color, (0, y), (self.SCREEN_WIDTH, y))
      
      pg.display.flip()

  def run(self):
    self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), vsync=1)
    self.clock = pg.time.Clock()
    self.createGridColors()
    print(self.obj_arr[0].grid_positions)

    while True:
      self.screen.fill(self.GREY)
      self.showGrid()
      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()

      for obj in self.obj_arr:
        self.update_pos(obj)
        pg.draw.circle(self.screen, self.WHITE, (obj.position[0], obj.position[1]), 1)
      
      pg.display.flip()
      
      self.clock.tick(40)
      pg.display.set_caption(str(self.clock.get_fps()))

## end TBS

if __name__ == "__main__":
  pg.init()
  TBS = TwoBodySimulation()
  TBS.run()