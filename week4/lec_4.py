# Naive search
import random

l = []
for i in range(10000):
  l.append(random.randint(0, 10000))

# a = 7
# l = [1, 2, 3, 4, 6, 8, 7]


n = 0
while n != -1:
  n = int(input("Enter a number: "))
  found = False
  for i in range(len(l)):
    if n == l[i]:
      print("Found at index", i)
      found = True
      break

  if found == False:
    print("Not found")

