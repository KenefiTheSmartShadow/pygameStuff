from vec2 import vec2
from Object import Object

class VectorGrid:
  def __init__(self):
    pass

  def setGridWeights(self, grid_index : int) -> list[vec2]:
    # make a vec2 for each cell of the grid
    local_grid_vector = []
    for cell in 2**grid_index:
      local_grid_vector.append(self.getVectors())
    return local_grid_vector

  def getVectors(self, obj_arr : list[Object]) -> vec2:
    """
    grid_depth is the amount of grids\n
    grid_index is the pos of the grid in the grid_depth grid\n
    Returns a vec2\n
    """
    total_obj_pos = vec2(0,0)
    for obj in obj_arr:
      total_obj_pos += obj.position
    cell_vector = total_obj_pos / len(obj_arr)
    return cell_vector
## end VectorGrid