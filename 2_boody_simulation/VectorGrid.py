from vec2 import vec2
from Object import Object

class VectorGrid:
  def __init__(self, size=1):
    """
    Makes a square grid from a given size\n
    size = amount of grid spaces on 1 side
    """
    self.grid_size = size
    self.vectorGridWeights = [[[] for _ in range(size)] for _ in range(size)]

    self.createDefualtValuesForCells()

  def setGridWeights(self, grid_depth : int, grid_index : int, obj_arr : list[Object]) -> list[vec2]:
    """
    Make a vec2 for each cell of the grid representing the 
    weight of where the majority of the objects inside of it are.\n
    grid_depth is the amount of grids\n
    grid_index is the pos of the grid in the grid_depth grid
    """
    local_grid_vector = []
    for cell in 2**grid_index:
      local_grid_vector.append(self.getVectorsForCell())
    return local_grid_vector

  def getVectorsForCell(self, obj_arr : list[Object]) -> vec2:
    """
    Returns a vec2\n
    """
    total_obj_pos = vec2(0,0)
    for obj in obj_arr:
      total_obj_pos += obj.position
    cell_vector = total_obj_pos / len(obj_arr)
    return cell_vector

  def createDefualtValuesForCells(self):
    for i in range(self.grid_size):
      for j in range(self.grid_size):
        self.vectorGridWeights[i][j] = vec2(0,0)

  def __iter__(self):
    self.current_row = 0
    self.current_col = 0
    return self
  def __next__(self):
    if self.current_row >= self.grid_size:
      raise StopIteration
    if self.current_col >= self.grid_size:
      self.current_row += 1
      self.current_col = 0
    cell = (self.current_row, self.current_col)
    self.current_col += 1
    return cell
## end VectorGrid

if __name__ == "__main__":
  vecGrid = VectorGrid(2)