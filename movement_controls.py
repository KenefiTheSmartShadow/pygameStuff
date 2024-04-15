import pygame as pg
import sys

class Character:
  def __init__(self, start_x=0, start_y=0, character_image=""):
    """Create a new character at (0,0)\n
    character_image should be a image file to use in place of the character
    it will be centered vertically and horizontally on the characters current
    position"""
    self.character_x, self.character_y = start_x, start_y
    self.char_image = ""
    if character_image != "":
      try:
        self.char_image = pg.image.load(character_image)
      except FileNotFoundError:
        print("ERROR: Could not find file" + character_image)
      except TypeError:
        print("ERROR: Could not find file" + character_image)

  def draw(self, screen):
    """draw the character on the screen"""
    self.moveFromKeyPress()
    if self.char_image == "":
      pg.draw.circle(screen, pg.Color(0,0,0), (self.character_x, self.character_y), 10)
    else:
      try:
        self.char_image = pg.image.load(self.char_image)
      except FileNotFoundError:
        print("ERROR: Could not find file" + self.char_image)
      except TypeError:
        print("ERROR: Could not find file" + self.char_image)

  def char_move(self, LRdir=1, x_multi=.5, UDdir=1, y_multi=.5):
    """LRdir: left(-1) or right(1, default)\n
    LRdir: up(-1) or down(1, default)"""
    self.character_x += LRdir * x_multi
    self.character_y += UDdir * y_multi

  def moveFromKeyPress(self):
    """left, right, up, down & wasd movement keys"""
    key = pg.key.get_pressed()
    if key[pg.K_LEFT] or key[pg.K_a]:
      self.char_move(LRdir=-1, UDdir=0)
    if key[pg.K_RIGHT] or key[pg.K_d]:
      self.char_move(LRdir=1, UDdir=0)
    if key[pg.K_UP] or key[pg.K_w]:
      self.char_move(LRdir=0, UDdir=-1)
    if key[pg.K_DOWN] or key[pg.K_s]:
      self.char_move(LRdir=0, UDdir=1)

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