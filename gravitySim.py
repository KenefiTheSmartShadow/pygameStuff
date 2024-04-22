import pygame as pg
import sys
import math

class Gravity:
  MAX_VELOCITY = 30

  def __init__(self, start_x=0, start_y=0, radius=10, color=(0,0,0)):
    self.character_x  = start_x
    self.character_y  = start_y
    self.radius       = radius
    self.velocity     = [5, 1]
    self.gravity      = [0, 0.1]
    self.color        = color
    self.surface_size = pg.display.get_window_size()

    self.max_pos, self.max_vel = self.surface_size[1],0
    self.basic_font   = pg.font.Font('freesansbold.ttf', 32)

  def get_pos(self):
    return "(" + str(math.floor(self.character_x * 100) / 100) + ", " + str(math.floor(self.character_y * 100) / 100) + ")"
  def get_vel(self):
    return "(" + str(math.floor(self.velocity[0] * 100) / 100) + ", " + str(math.floor(self.velocity[1] * 100) / 100) + ")"
  def get_max_pos(self):
    self.max_pos = self.character_y if self.character_y < self.max_pos else self.max_pos
    return str(self.max_pos)
  def get_max_vel(self):
    self.max_vel = self.velocity[1] if self.velocity[1] < self.max_vel else self.max_vel
    return str(abs(self.max_vel))

  def render_debug(self, screen):
    char_pos = self.basic_font.render(self.get_pos(), True, (0,0,0))
    char_vel = self.basic_font.render(self.get_vel(), True, (0,0,0))

    posRect = char_pos.get_rect()
    velRect = char_vel.get_rect()
    posRect.center = (400, 300-16)
    velRect.center = (400, 300+16)

    max_pos = self.basic_font.render(self.get_max_pos(), True, (0,0,0))
    max_vel = self.basic_font.render(self.get_max_vel(), True, (0,0,0))

    maxPosRect = max_pos.get_rect()
    maxVelRect = max_vel.get_rect()
    maxPosRect.center = (400, 300-48)
    maxVelRect.center = (400, 300-80)

    screen.blit(char_pos, posRect)
    screen.blit(char_vel, velRect)
    screen.blit(max_pos, maxPosRect)
    screen.blit(max_vel, maxVelRect)

  def draw(self, screen: pg.Surface):
    self.char_move()
    self.check_valid_pos()
    self.render_debug(screen)
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
    temp_vel = self.velocity
    if self.character_x < 0 + self.radius or self.character_x > self.surface_size[0] - self.radius:
      self.velocity[0] *= -1
      self.character_x = 0 + self.radius if self.character_x < self.surface_size[0] / 2 else self.surface_size[0] - self.radius
      # self.velocity[0] = temp_vel[0] * -1
    if self.character_y < 0 + self.radius or self.character_y > self.surface_size[1] - self.radius:
      self.velocity[1] *= -1
      self.character_y = 0 + self.radius if self.character_y < self.surface_size[1] / 2 else self.surface_size[1] - self.radius
      # self.velocity[1] = temp_vel[1] * -1

# end Gravity

def main():
  pg.init()
  screen = pg.display.set_mode((800, 600))
  clock = pg.time.Clock()
  char = Gravity(400, 550, 10, 0)

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
