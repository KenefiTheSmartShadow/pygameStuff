import pygame as pg
import sys
import math
import random

class Gravity:
  MAX_VELOCITY   = 30
  AIR_RESISTANCE = .1

  def __init__(self, velocity : list[int], start_x=0, start_y=0, radius=10, color=(0,0,0), control=0, debug=1):
    self.character_x  = start_x
    self.character_y  = start_y
    self.radius       = radius
    self.velocity     = velocity
    self.gravity      = [0, 0.3]
    self.color        = color
    self.surface_size = pg.display.get_window_size()
    self.control      = control
    self.debug        = debug

    self.max_pos, self.max_vel = self.surface_size[1],0
    self.basic_font   = pg.font.Font('freesansbold.ttf', 32)

  def char_move_from_press(self, move_multiplier, LRdir=1, UDdir=1):
    """LRdir: left(-1) or right(1, default)\n
    LRdir: up(-1) or down(1, default)"""
    self.velocity[1] += self.gravity[1]
    self.velocity[0] += LRdir * move_multiplier
    self.velocity[1] += UDdir * move_multiplier
    if self.velocity[0] > self.MAX_VELOCITY:
      self.velocity[0] = self.MAX_VELOCITY
    if self.velocity[1] > self.MAX_VELOCITY:
      self.velocity[1] = self.MAX_VELOCITY
    if self.velocity[0] < -self.MAX_VELOCITY:
      self.velocity[0] = -self.MAX_VELOCITY
    if self.velocity[1] < -self.MAX_VELOCITY:
      self.velocity[1] = -self.MAX_VELOCITY

  def move_from_key_press(self):
    """left, right, up, down & wasd movement keys"""
    key = pg.key.get_pressed()

    # sprint and crouch
    move_multi = 3
    if key[pg.K_LCTRL] and key[pg.K_LSHIFT]:
      move_multi = 0.5
    elif key[pg.K_LCTRL]:
      move_multi = 0.25
    elif key[pg.K_LSHIFT]:
      move_multi = 0.75

    # wasd and arrow keys
    if key[pg.K_LEFT] or key[pg.K_a]:
      self.char_move_from_press(move_multi, LRdir=-1, UDdir= 0)
    if key[pg.K_RIGHT] or key[pg.K_d]:
      self.char_move_from_press(move_multi, LRdir= 1, UDdir= 0)
    if key[pg.K_UP] or key[pg.K_w]:
      self.char_move_from_press(move_multi, LRdir= 0, UDdir=-1)
    if key[pg.K_DOWN] or key[pg.K_s]:
      self.char_move_from_press(move_multi, LRdir= 0, UDdir= 1)

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

    screen.blit(char_pos, posRect)
    screen.blit(char_vel, velRect)

    # max_pos = self.basic_font.render(self.get_max_pos(), True, (0,0,0))
    # max_vel = self.basic_font.render(self.get_max_vel(), True, (0,0,0))

    # maxPosRect = max_pos.get_rect()
    # maxVelRect = max_vel.get_rect()
    # maxPosRect.center = (400, 300-48)
    # maxVelRect.center = (400, 300-80)

    # screen.blit(max_pos, maxPosRect)
    # screen.blit(max_vel, maxVelRect)

  def update_velocity(self):
    if self.velocity[0] > 0:
      self.velocity[0] -= self.AIR_RESISTANCE
    if self.velocity[1] > 0:
      self.velocity[1] -= self.AIR_RESISTANCE
    if self.velocity[0] < 0:
      self.velocity[0] += self.AIR_RESISTANCE
    if self.velocity[1] < 0:
      self.velocity[1] += self.AIR_RESISTANCE

    self.velocity[0] = int(self.velocity[0]*10)/10
    self.velocity[1] = int(self.velocity[1]*10)/10

  def draw(self, screen: pg.Surface):
    self.update_velocity()
    self.check_valid_pos()
    if self.control:
      self.move_from_key_press()
    self.char_move()
    if self.debug:
      self.render_debug(screen)
    pg.draw.circle(screen, pg.Color(self.color), (self.character_x, self.character_y), self.radius)

  def char_move(self):
    self.velocity[1] += self.gravity[1]
    self.character_x += self.velocity[0]
    self.character_y += self.velocity[1]
    if self.velocity[0] > self.MAX_VELOCITY:
      self.velocity[0] = self.MAX_VELOCITY
    if self.velocity[1] > self.MAX_VELOCITY:
      self.velocity[1] = self.MAX_VELOCITY
    if self.velocity[0] < -self.MAX_VELOCITY:
      self.velocity[0] = -self.MAX_VELOCITY
    if self.velocity[1] < -self.MAX_VELOCITY:
      self.velocity[1] = -self.MAX_VELOCITY

  def check_valid_pos(self):
    # temp_vel = self.velocity
    if self.character_x < 0 + self.radius or self.character_x > self.surface_size[0] - self.radius:
      self.velocity[0] *= 0
      self.character_x = 0 + self.radius if self.character_x < self.surface_size[0] / 2 else self.surface_size[0] - self.radius
      # self.velocity[0] = temp_vel[0] * -1
    if self.character_y < 0 + self.radius or self.character_y > self.surface_size[1] - self.radius:
      self.velocity[1] *= 0
      self.character_y = 0 + self.radius if self.character_y < self.surface_size[1] / 2 else self.surface_size[1] - self.radius
      # self.velocity[1] = temp_vel[1] * -1
# end Gravity

def collision(one, other):
  dx = one.character_x - other.character_x
  dy = one.character_y - other.character_y
  distance = math.sqrt(dx**2 + dy**2) + .000001

  # Check if the distance is less than the sum of the radii
  if distance < one.radius + other.radius:
    # Calculate overlap
    overlap = 0.5 * (distance - one.radius - other.radius)

    # Displace current object
    one.character_x -= overlap * (one.character_x - other.character_x) / distance
    one.character_y -= overlap * (one.character_y - other.character_y) / distance

    # Displace other object
    other.character_x += overlap * (one.character_x - other.character_x) / distance
    other.character_y += overlap * (one.character_y - other.character_y) / distance

    # Assuming a perfectly elastic collision
    # Update velocities
    one.velocity[0], other.velocity[0] = other.velocity[0], one.velocity[0]
    one.velocity[1], other.velocity[1] = other.velocity[1], one.velocity[1]

def fixed_grid_collision(char_arr : list[Gravity]):
  surface_size = pg.display.get_window_size()
  """
  Create a grid
  get the balls that are in each grid square
  calculate for those and surounding squares
  """
  grid = [[[] for _ in range(int(surface_size[0]/20))] for _ in range(int(surface_size[1]/20))]
  i = 0
  for obj in char_arr:
    x = int(math.floor((obj.character_x - 1) / 20))
    y = int(math.floor((obj.character_y - 1) / 20))
    x = 39 if x > 39 else x
    y = 39 if y > 39 else y
    grid[y][x].append(i)
    i += 1
  # print(grid)

  """
  loop through the grid
  for each grid cell calculate its and the surounding cells collisions
  """
  for grid_x in range(len(grid)):
    for grid_y in range(len(grid[grid_x])):
      for i in range(max(0, grid_x-1), min(len(grid), grid_x+2)):
        for j in range(max(0, grid_y-1), min(len(grid[grid_x]), grid_y+2)):
          for a in range(len(grid[grid_x][grid_y])):
            for b in range(len(grid[i][j])):
              if grid[grid_x][grid_y][a] != grid[i][j][b]:
                collision(char_arr[grid[grid_x][grid_y][a]], char_arr[grid[i][j][b]])

# threading

def main():
  pg.init()
  WIDTH, HEIGHT = 800, 800
  screen = pg.display.set_mode((WIDTH, HEIGHT))
  clock = pg.time.Clock()
  surface_size = pg.display.get_window_size()

  num_obj = 500
  char_arr = []

  char = Gravity([0,0], radius=5, control=0, debug=0)
  char_arr.append(char)

  for i in range(1, num_obj + 1):
    rand_x, rand_y = random.randint(0, surface_size[0]), random.randint(0, surface_size[1])
    rand_x_vel, rand_y_vel = 0, 0 # random.randint(-5, 5), random.randint(0, 5)
    rand_radius = 5 # random.randint(10,200) / 10
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
      obj.draw(screen)
    fixed_grid_collision(char_arr)
    pg.display.flip()

    clock.tick(60)

if __name__ == "__main__":
  main()
