import math


class Point():

  def __init__(self, x=0, y=0) -> None:
    self.x = x
    self.y = y

  def move(self, dx, dy):
    self.x += dx
    self.y += dy

  def value(self):
    return (self.x, self.y)

  def duplicate(self):
    return Point(self.x, self.y)


class Line():

  def __init__(self, startPoint, endPoint) -> None:
    self.startPoint = startPoint
    self.endPoint = endPoint

  def length(self):
    return math.sqrt((self.startPoint.x - self.endPoint.x)**2 +
                     (self.startPoint.y - self.endPoint.y)**2)

  def slope(self):
    if self.startPoint.x == self.endPoint.x:
      return math.inf

    return ((self.startPoint.y - self.endPoint.y) /
            (self.startPoint.x - self.endPoint.x))


pt1 = Point()
pt2 = pt1.duplicate()

inp1 = input().strip().split(',')
inp2 = input().strip().split(',')

pt1.move(int(inp1[0]), int(inp1[1]))
pt2.move(int(inp2[0]), int(inp2[1]))

print(f'Point 1: {pt1.value()}')
print(f'Point 2: {pt2.value()}')

l1 = Line(pt1, pt2)
print(f'Line length: {l1.length():.2f}')
print(f'Line slope: {l1.slope():.2f}')
