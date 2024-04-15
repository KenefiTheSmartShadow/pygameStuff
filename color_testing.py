import pygame as pg
import sys
from pygame.locals import *

import time
cur_time = time.time()

red = [255, 128, 0]
red_add = [1.5, 2, 3.5]

def change_color():
    red[0] = red[0] + red_add[0]
    red[1] = red[1] + red_add[1]
    red[2] = red[2] + red_add[2]
    for color in range(0, 3):
      red[color] *= cur_time / red_add[color]
      red[color] %= 255

pg.init()
screen = pg.display.set_mode((600,600))
display_dimentions = pg.display.get_window_size()
display_width, display_height = display_dimentions[0], display_dimentions[1] 
display_area = display_height * display_width

try:
  while True:
    cur_time = time.time()
    for event in pg.event.get():
      if event.type == QUIT:
        pg.quit()
        sys.exit()
    change_color()
    screen.fill(red)
    pg.display.flip()
    time.sleep(1)
except ValueError:
  print("ERROR")