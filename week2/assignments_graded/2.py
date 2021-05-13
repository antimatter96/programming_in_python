x = int(input())
if x < 0 or x > 23:
    print("INVALID")
elif x >= 18:
    print("EVENING")
elif x >= 12:
    print("AFTERNOON")
elif x >= 6:
    print("MORNING")
elif x >= 0:
    print("NIGHT")
