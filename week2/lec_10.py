# intro to import

# Library function

import math

print(math.log(10))
print(math.sin(31.41))
print(math.sqrt(10))
print(math.factorial(5))

# this means that math is a library
# we can use functions / constants in math
# not auto fetch => costly
# use `math` everywhere 

import random

print(random.random())

# simulate a coin toss

a = random.random()
if a < 0.5:
  print("Heads")
else:
  print("Tails")

# simulate a dice

print(random.randrange(1, 7))

# simulate two dices

x = random.randrange(1, 7)
y = random.randrange(1, 7)

print("sum", x + y)
