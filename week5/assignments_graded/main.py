#Import math Library
import math

#print the Euclidean norm for the given points
print(math.hypot(10, 2, 4, 13))
print(math.hypot(4, 7, 8))
print(math.hypot(12, 14))
print(math.hypot())


# def assert(x):
#   return x == int(str(x))
# assert(1)

def f():
  return x
x = 10.0
print(f())

def f():
  print(n)

n = 5
f()

s = math.sqrt
print(s(190))

import random
x = random.random()
for i in range(4):
  print(x)

##
# x = 0
#   f(0) => 0
#   g(0) => 0

# x = 1
#   f(1) => f(0) => 0
#   g(1) => g(-1) => g(-3) => ERROR

# x = 2
#   f(2) => f(1) => 0
#   g(2) => g(0) => 0

# x = 3
#   f(3) => f(2) => 0
#   g(3) => g(1) => ERROR

# x = 4
#   f(4) => f(3) => 0
#   g(4) => g(2) => 0

# x = 5
#   f(5) => f(4) => 0
#   g(5) => g(3) => ERROR

# x = 6
#   f(6) => g(4) => 0
#   g(6) => f(5) => 0

# x = 7
#   f(7) => g(5) => ERROR
#   g(7) => f(6) => 0

# x = 8
#   f(8) => g(6) => 0
#   g(8) => f(7) => ERROR

# x = 9
#   f(9) => g(7) => 0
#   g(9) => f(8) => 0

# x = 10
#   f(10) => g(8) => ERROR
#   g(10) => f(9) => 0
