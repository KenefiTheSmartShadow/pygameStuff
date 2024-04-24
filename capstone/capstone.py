import pygame as pg
import sys

WHITE = (255,255,255)
BLACK = (200,200,200)

def spiral(screen):
  x, y = 880, 455  # Starting position
  length = 400
  angle = 0  # Start with a horizontal line

  for i in range(0, int(length/20)):  # Increase the number of lines to draw
    if angle == 0:  # Horizontal right
      pg.draw.line(screen, BLACK, (x, y), (x + length + 10, y), 20)
      x += length
    elif angle == 90:  # Vertical down
      pg.draw.line(screen, BLACK, (x, y), (x, y + length + 10), 20)
      y += length
    elif angle == 180:  # Horizontal left
      pg.draw.line(screen, BLACK, (x, y), (x - length - 10, y), 20)
      x -= length
    elif angle == 270:  # Vertical up
      pg.draw.line(screen, BLACK, (x, y), (x, y - length - 10), 20)
      y -= length

    angle = (angle + 90) % 360  # Change direction
    length -= 20  # Decrease the length for the next line

def sunset_effect(image : pg.Surface):
  image_w, image_h = image.get_size()[0], image.get_size()[1]
  for i in range(image_w):
    for j in range(image_h):
      color = image.get_at((i,j))
      # print(color)
      color.r = 255 if int(color.r * 1.3) > 255 else int(color.r * 1.3)
      image.set_at((i,j), color)

def grey_scale(image : pg.Surface):
  # gray = 0.2126 × red + 0.7152 × green + 0.0722 × blue
  image_w, image_h = image.get_size()[0], image.get_size()[1]
  for i in range(image_w):
    for j in range(image_h):
      color = image.get_at((i,j))
      # print(color)
      grey = int(color.r * .2126 + color.g * .7152 + color.b * .0722)
      image.set_at((i,j), (grey, grey, grey))

def main():
  pg.init()

  WIDTH, HEIGHT = 1560, 850

  screen = pg.display.set_mode((WIDTH, HEIGHT))
  screen.fill(WHITE)
  spiral(screen)

  imag = pg.image.load("non-sunset.jpg")
  imag2 = pg.image.load("2.jpg")
  sunset_effect(imag)
  grey_scale(imag2)
  screen.blit(imag, (0,0))
  screen.blit(imag2, (880,0))

  pg.display.flip()

  while True:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
  


if __name__ == "__main__":
  main()