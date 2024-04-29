import pygame as pg
import math
from Character import Character

class CollisionDetection:
  def check_collision(char_1 : Character, char_2 : Character):
    # if the 2 overlap move them linearly apart from each other until they don't collide
    dist = math.sqrt((char_1.character_x - char_2.character_x)**2 + (char_1.character_y - char_2.character_y)**2)

    if dist < char_1.radius + char_2.radius:
      return True
    return False
  
  def resolve_collision(char_1, char_2):
    dx = char_1.character_x - char_2.character_x
    dy = char_1.character_y - char_2.character_y
    distance = math.sqrt(dx*dx + dy*dy)
    overlap = char_1.radius + char_2.radius - distance

    if distance == 0:
       distance += .0000001

    if overlap > 0:
        # Normal vector
        normal = [dx/distance, dy/distance]

        # Move the characters apart along the normal vector
        char_1.character_x += normal[0] * overlap / 2
        char_1.character_y += normal[1] * overlap / 2
        char_2.character_x -= normal[0] * overlap / 2
        char_2.character_y -= normal[1] * overlap / 2

        # Calculate relative velocity
        rel_velocity = [char_1.character_x - char_1.character_x, char_1.character_y - char_1.character_y]

        # Project velocity onto the normal vector
        vel_along_normal = rel_velocity[0] * normal[0] + rel_velocity[1] * normal[1]

        # If objects are moving towards each other
        if vel_along_normal < 0:
            # Reverse their velocity along the normal vector
            char_1.character_x -= vel_along_normal * normal[0]
            char_1.character_y -= vel_along_normal * normal[1]
            char_2.character_x += vel_along_normal * normal[0]
            char_2.character_y += vel_along_normal * normal[1]

def main():
  pass
if __name__ == "__main__":
  main()