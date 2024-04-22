import pygame as pg
import sys
import math
import random

class Gravity:
  MAX_VELOCITY = 30

  def __init__(self, velocity : list[int], start_x=0, start_y=0, radius=10, color=(0,0,0), debug=1):
    self.character_x  = start_x
    self.character_y  = start_y
    self.radius       = radius
    self.velocity     = velocity
    self.gravity      = [0, 0.1]
    self.color        = color
    self.surface_size = pg.display.get_window_size()
    self.debug        = debug

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
    if self.debug:
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

  def check_collision(self, other):
    dx = self.character_x - other.character_x
    dy = self.character_y - other.character_y
    distance = math.sqrt(dx**2 + dy**2)

    # Check if the distance is less than the sum of the radii
    if distance < self.radius + other.radius:
      # Calculate overlap
      overlap = 0.5 * (distance - self.radius - other.radius)

      # Displace current object
      self.character_x -= overlap * (self.character_x - other.character_x) / distance
      self.character_y -= overlap * (self.character_y - other.character_y) / distance

      # Displace other object
      other.character_x += overlap * (self.character_x - other.character_x) / distance
      other.character_y += overlap * (self.character_y - other.character_y) / distance

      # Assuming a perfectly elastic collision
      # Update velocities
      self.velocity[0], other.velocity[0] = other.velocity[0], self.velocity[0]
      self.velocity[1], other.velocity[1] = other.velocity[1], self.velocity[1]

      return True
    return False

# end Gravity

def main():
  pg.init()
  screen = pg.display.set_mode((800, 600))
  clock = pg.time.Clock()

  num_obj = 200
  char_arr = []
  surface_size = pg.display.get_window_size()
  for i in range(0, num_obj):
    rand_x, rand_y = random.randint(0, surface_size[0]), random.randint(0, surface_size[1])
    rand_x_vel, rand_y_vel = random.randint(0, 5), random.randint(0, 5)
    rand_radius = random.randint(10,200) / 10
    new_vel = [rand_x_vel, rand_y_vel]
    char_arr.append(Gravity(new_vel, rand_x, rand_y, rand_radius, debug=0))
    char_arr[i].color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

  WHITE = (255, 255, 255)

  while True:
    screen.fill(WHITE)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

    for obj in char_arr:
      for other in char_arr:
        if obj == other:
          continue
        obj.check_collision(other)
      obj.draw(screen)
    pg.display.flip()

    # clock.tick(60)

if __name__ == "__main__":
  main()
