import pygame as pg
import sys

class Character:
  def __init__(self, start_x=0, start_y=0):
    """Create a new character at (0,0)"""
    self.character_x, self.character_y = start_x, start_y

  def draw(self, screen):
    """draw the character on the screen\n
    needs a screen variable from pygame"""
    self.move_from_key_press()
    # catch if the player is outside of the screen bounds
    self.check_valid_pos()
    pg.draw.circle(screen, pg.Color(0,0,0), (self.character_x, self.character_y), 10)

  def char_move(self, move_multiplier, LRdir=1, UDdir=1):
    """LRdir: left(-1) or right(1, default)\n
    LRdir: up(-1) or down(1, default)"""
    self.character_x += LRdir * move_multiplier
    self.character_y += UDdir * move_multiplier

  def move_from_key_press(self):
    """left, right, up, down & wasd movement keys"""
    key = pg.key.get_pressed()

    # sprint and crouch
    move_multi = 0.5
    if key[pg.K_LCTRL] and key[pg.K_LSHIFT]:
      move_multi = 0.5
    elif key[pg.K_LCTRL]:
      move_multi = 0.25
    elif key[pg.K_LSHIFT]:
      move_multi = 0.75

    # wasd and arrow keys
    if key[pg.K_LEFT] or key[pg.K_a]:
      self.char_move(move_multi, LRdir=-1, UDdir=0)
    if key[pg.K_RIGHT] or key[pg.K_d]:
      self.char_move(move_multi, LRdir=1, UDdir=0)
    if key[pg.K_UP] or key[pg.K_w]:
      self.char_move(move_multi, LRdir=0, UDdir=-1)
    if key[pg.K_DOWN] or key[pg.K_s]:
      self.char_move(move_multi, LRdir=0, UDdir=1)

  def check_valid_pos(self):
    # if the character goes off screen put it back on the edge
    surface_size = pg.display.get_window_size()
    if self.character_x < 0 or self.character_x > surface_size[0]:
      self.character_x = 0 if self.character_x < surface_size[0] / 2 else surface_size[0]
    if self.character_y < 0 or self.character_y > surface_size[1]:
      self.character_y = 0 if self.character_y < surface_size[1] / 2 else surface_size[1]

# end Character


def main():
  WIDTH, HEIGHT = 800, 600

  pg.init()
  screen = pg.display.set_mode((WIDTH, HEIGHT))
  char = Character()
  
  WHITE = (255, 255, 255)

  while True:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
  
    screen.fill(WHITE)
    char.draw(screen)
    pg.display.flip()
  


if __name__ == "__main__":
  main()