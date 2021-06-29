# Tutorial
import math
# Calculate no of upper, lower, total, words

def count_upper(sentence:str):
  count = 0
  for c in sentence:
    if c.isupper():
      count += 1
  return count

def count_lower(sentence:str):
  count = 0
  for c in sentence:
    if c.islower():
      count += 1
  return count

def count_char(sentence:str):
  return len(sentence)

def count_words(sentence:str):
  count = 1
  for char in sentence:
    if char == ' ':
      count+=1
  return count

def calc(sentence:str):
  return count_upper(sentence), count_lower(sentence), count_char(sentence), count_words(sentence)

test_cases = ["AB CD EF gh ijkl"]
for tc in test_cases:
  no_of_upper, no_of_lower, total_characters, total_words = calc(tc)
  # print("no_of_upper: {}\nno_of_lower: {}\ntotal_characters: {}\ntotal_words: {}".format(no_of_upper, no_of_lower, total_characters, total_words))

#--------------------

# calc perimeter, area of circle, recatngle
# menu driven

CIRCLE = "circle"
RECTANGLE = "rectangle"

AREA = "area"
PERIMETER = "perimeter"

def area_circle(r):
  return math.pi * r * r

def perimeter_circle(r):
  return 2 * math.pi * r

def perimeter_rec(a, b):
  return 2 * (a + b)

def area_rec(a, b):
  return a * b

shape = "exit"
while shape != "exit":
  print("Enter shape : [circle rectangle exit]")
  shape = str(input("Shape (enter `exit` to exit): "))

  if shape == "exit":
    break

  print("Enter operation : [area perimeter exit]")
  operation = str(input("Operation : "))

  if shape == CIRCLE:
    r = float(input("Radius : "))
  elif shape == RECTANGLE:
    l = float(input("Length : "))
    b = float(input("Breadth : "))
  else:
    break

  if shape == CIRCLE and operation == AREA:
    ans = area_circle(r)
  elif shape == CIRCLE and operation == PERIMETER:
    ans = perimeter_circle(r)
  elif shape == RECTANGLE and operation == AREA:
    ans = area_rec(l, b)
  elif shape == RECTANGLE and operation == PERIMETER:
    ans = perimeter_rec(l, b)
  print("{:10s} of {:10s} is : {:.2f}".format(operation, shape,ans))

#------------------

# 3 points => triangle or not
# slope of line AND length

def accept_point(n):
  print("Enter coordinates of point", n)
  return float(input("Enter x coordinate : ")), float(input("Enter y coordinate : "))

def dist(x1, y1, x2, y2):
  return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

def check_triangle_dist(x1, y1, x2, y2, x3, y3):
  a = dist(x1, y1, x2, y2)
  b = dist(x2, y2, x3, y3)
  c = dist(x3, y3, x1, y1)

  if a + b <= c or b + c <= a or c + a <= b:
    print("Invalid")
  else:
    print("Valid")

def slope(x1, y1, x2, y2):
  if x1 == x2:
    return -math.inf
  return (y2-y1)/(x2-x1)

def check_triangle_slope(x1, y1, x2, y2, x3, y3):
  m1 = slope(x1, y1, x2, y2)
  m2 = slope(x2, y2, x3, y3)
  m3 = slope(x3, y3, x1, y1)
  if m1 == m2 or m2 == m3 or m3 == m1:
    print("Invalid")
  else:
    print("Valid")

x1, y1 = accept_point(1)
x2, y2 = accept_point(2)
x3, y3 = accept_point(3)

check_triangle_dist(x1, y1, x2, y2, x3, y3)
check_triangle_slope(x1, y1, x2, y2, x3, y3)
