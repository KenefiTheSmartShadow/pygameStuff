import pygame as pg
import sys

from Character import Character

class ImageCharacter(Character):
  def __init__(self, screen : pg.Surface, file_ref : str, start_x=0, start_y=0):
    super().__init__(start_x, start_y)

    self.image_name = file_ref
    self.source = pg.image.load(self.image_name)
    self.image_size = self.source.get_size
    self.open_file(screen)

  def open_file(self, screen):
    try:
      self.draw(screen)
    except pg.error as e:
      print("Error loading image:", e)

  def draw(self, screen):
    self.move_from_key_press()
    self.check_valid_pos()
    screen.blit(self.source, (self.character_x, self.character_y))

  def move_from_key_press(self):
    return super().move_from_key_press()
  
  def char_move(self, move_multiplier, LRdir=1, UDdir=1):
    return super().char_move(move_multiplier, LRdir, UDdir)
  
  def check_valid_pos(self):
    surface_size = pg.display.get_window_size()
    if self.character_x < 0 or self.character_x > surface_size[0] - self.source.get_width():
      self.character_x = 0 if self.character_x < surface_size[0] / 2 else surface_size[0] - self.source.get_width()
    if self.character_y < 0 or self.character_y > surface_size[1] - self.source.get_height():
      self.character_y = 0 if self.character_y < surface_size[1] / 2 else surface_size[1] - self.source.get_height()
## end ImageTesting

def main():
  WIDTH, HEIGHT = 800, 600
  screen = pg.display.set_mode((WIDTH, HEIGHT))

  pg.init()
  imag = ImageCharacter(screen, "smile.png", 400, 300)

  WHITE = (255, 255, 255)
  
  while True:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
  
    screen.fill(WHITE)
    imag.draw(screen)
    pg.display.flip()
  
if __name__ == "__main__":
  main()