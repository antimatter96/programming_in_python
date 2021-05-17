## print prime factors of a numbers
x = int(input())
y = x
for i in range(2, x + 1, 1):
    if y % i == 0:
        print(i)
        while y%i == 0:
            y = y//i
