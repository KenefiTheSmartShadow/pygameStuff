import pygame as pg
import sys

class Gravity:
  MAX_VELOCITY = 30

  def __init__(self, start_x=0, start_y=0, radius=10, controlleable=1, color=(0,0,0)):
    self.character_x = start_x
    self.character_y = start_y
    self.radius = radius
    self.controlleable = controlleable
    self.velocity = [5, 1]
    self.gravity = [0, 0.1]
    self.color = color

  def draw(self, screen: pg.Surface):
    self.char_move()
    self.check_valid_pos()

    if self.controlleable:
      self.move_from_key_press()
    pg.draw.circle(screen, pg.Color(self.color), (self.character_x, self.character_y), self.radius)

  def char_move(self):
    self.velocity[1] += self.gravity[1]
    self.character_x += self.velocity[0]
    self.character_y += self.velocity[1]

  def update_velocity(self, vel_modif):
    self.velocity[1] += vel_modif
    if self.velocity[0] > self.MAX_VELOCITY:
      self.velocity[0] = self.MAX_VELOCITY
    if self.velocity[1] > self.MAX_VELOCITY:
      self.velocity[1] = self.MAX_VELOCITY

  def check_valid_pos(self):
    surface_size = pg.display.get_window_size()
    if self.character_x < 0 + self.radius or self.character_x > surface_size[0] - self.radius:
      self.velocity[0] *= -1
    if self.character_y < 0 + self.radius or self.character_y > surface_size[1] - self.radius:
      self.velocity[1] *= -1

    

def main():
  pg.init()
  char = Gravity(400, 300, 10, 0)
  while True:
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    WHITE = (255, 255, 255)

    while True:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()

      screen.fill(WHITE)
      char.draw(screen)
      pg.display.flip()

      clock.tick(60)

if __name__ == "__main__":
  main()
