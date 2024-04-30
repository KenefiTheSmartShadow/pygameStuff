class vec2:
  def __init__(self, x: float, y: float):
    self.x_vector = x
    self.y_vector = y

  def __add__(self, other) -> 'vec2':
    return vec2(self.x_vector + other.x_vector, self.y_vector + other.y_vector)

  def __sub__(self, other) -> 'vec2':
    return vec2(self.x_vector - other.x_vector, self.y_vector - other.y_vector)

  def __mul__(self, scalar: float) -> 'vec2':
    if isinstance(scalar, (int, float)):  # Scalar multiplication
      return vec2(self.x_vector * scalar, self.y_vector * scalar)
    raise TypeError("Multiplication with non-scalar is not supported")

  def __truediv__(self, scalar: float) -> 'vec2':
    if isinstance(scalar, (int, float)):  # Scalar division
      return vec2(self.x_vector / scalar, self.y_vector / scalar)
    raise TypeError("Division by non-scalar is not supported")

  def __getitem__(self, index) -> float:
    match index:
      case 0:
        return self.x_vector
      case 1:
        return self.y_vector
      
  def __str__(self):
    return("(" + str(self.x_vector) + ", " + str(self.y_vector) + ")")

  def dot(self, other) -> float:
    return self.x_vector * other.x_vector + self.y_vector * other.y_vector

  def cross(self, other) -> float:
    # In 2D, cross product results in a scalar representing the z-component of the perpendicular vector
    return self.x_vector * other.y_vector - self.y_vector * other.x_vector

  def magnitude(self) -> float:
    return (self.x_vector**2 + self.y_vector**2)**0.5

  def normalize(self) -> 'vec2':
    mag = self.magnitude()
    return vec2(self.x_vector / mag, self.y_vector / mag)
## end vec2