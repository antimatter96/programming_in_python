x, y = float(input()), float(input())
if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-axis")
elif y == 0:
    print("X-axis")
elif x > 0 and y > 0:
    print("I")
elif x > 0 and y < 0:
    print("IV")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
