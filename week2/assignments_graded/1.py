x, y, z = int(input()), int(input()), int(input())
if x + y <= z:
    print("NO")
elif y + z <= x:
    print("NO")
elif z + x <= y:
    print("NO")
else:
    print("YES")
