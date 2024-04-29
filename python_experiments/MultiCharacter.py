import pygame as pg
import sys
import random
import Character
import ImageCharacter

class MultiObj:
  def __init__(self, num_objects):
    self.num_obj = num_objects
    self.generate_characters()

  def generate_characters(self):
    """
    Create an array of Characters with unique colors and posistions
    """
    self.char_arr = []
    surface_size = pg.display.get_window_size()
    for i in range(0, self.num_obj):
      rand_x, rand_y = random.randint(0, surface_size[0]), random.randint(0, surface_size[1])
      self.char_arr.append(Character.Character(rand_x, rand_y))
      self.char_arr[i].color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

  def draw(self, screen : pg.Surface):
    for obj in range(0, self.num_obj):
      x_pos, y_pos = self.char_arr[obj].character_x, self.char_arr[obj].character_y
      pg.draw.circle(screen, pg.Color(self.char_arr[obj].color), (x_pos, y_pos), 10)

  def change_position(self):
    surface_size = pg.display.get_window_size()
    for obj in range(0, self.num_obj):
      self.char_arr[obj].character_x, self.char_arr[obj].character_y = random.randint(0, surface_size[0]), random.randint(0, surface_size[1])

## end MultiObj

class MultiImageObj(MultiObj):
  def __init__(self, screen : pg.Surface, num_objects, file_ref : str):
    self.num_obj = num_objects
    self.file_ref = file_ref
    self.generate_characters(screen)

  def generate_characters(self, screen):
    self.char_arr = []
    surface_size = pg.display.get_window_size()
    for i in range(0, self.num_obj):
      rand_x, rand_y = random.randint(0, surface_size[0]), random.randint(0, surface_size[1])
      self.char_arr.append(ImageCharacter.ImageCharacter(screen, self.file_ref, rand_x, rand_y))

  def draw(self, screen : pg.Surface):
    for i in range(0, self.num_obj):
      x_pos, y_pos = self.char_arr[i].character_x, self.char_arr[i].character_y
      screen.blit(self.char_arr[i].source, (x_pos, y_pos))

  def change_position(self):
    return super().change_position()
## end MultiImageObj

def main():
  WIDTH, HEIGHT = 800, 600

  pg.init()
  screen = pg.display.set_mode((WIDTH, HEIGHT))
  char = MultiImageObj(screen, 100, "smile.png")
  char2 = MultiObj(100)
  
  WHITE = (255, 255, 255)

  while True:
    key = pg.key.get_pressed()
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

    if key[pg.K_r]:
      char.change_position()
      char2.change_position()

    screen.fill(WHITE)
    char.draw(screen)
    char2.draw(screen)
    pg.display.flip()

if __name__ == '__main__':
  main()