a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

if (a+b)%2 != 0:
  print("NO")
elif (b+c)%2 != 0:
  print("NO")
elif (c+d)%2 != 0:
  print("NO")
elif (d+e)%2 != 0:
  print("NO")
elif (e+a)%2 != 0:
  print("NO")
else:
  print("YES")
