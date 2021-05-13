x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3 = float(input())

if x1 == x2:
  print("Vertical Line")
else:
  m = (y2-y1)/(x2-x1)
  c = y1 - (m*x1)
  y3 = (m * x3) + c
  print(y3)
  if m == 0:
    print("Horizontal Line")
  elif m > 0:
    print("Positive Slope")
  else:
    print("Negative Slope")
