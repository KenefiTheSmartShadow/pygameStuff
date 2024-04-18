import pygame as pg
import sys
from Character import Character
from CollisionDetection import CollisionDetection

WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)

def main():
  WIDTH, HEIGHT = 800, 600

  pg.init()
  screen = pg.display.set_mode((WIDTH, HEIGHT))
  char = Character()
  char_2 = Character(start_x=50, start_y=50, controlleable=0)
  char_2.color = BLACK
  char_3 = Character(start_x=100, start_y=100, radius=20, controlleable=0)
  
  while True:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
  
    if CollisionDetection.check_collision(char, char_2):
      CollisionDetection.resolve_collision(char, char_2)
      char.color = GREEN
    else:
      char.color = BLACK

    screen.fill(WHITE)
    
    char.draw(screen)
    char_2.draw(screen)
    pg.display.flip()

main()