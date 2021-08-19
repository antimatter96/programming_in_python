# Functional Part 1

fruits = ["mango", "apple", "A", "b", "c", "d", "E"]

for fruit in fruits:
  print(fruit)

## What if we want to add timeout or want to process them one by one
## How to pass around the basket state
## ITERATORS

basket = iter(fruits)

print(basket) # <list_iterator onbuect>

print(next(basket)) # [prints mango]

##..
##..

print(next(basket)) # [prints apple]

##..
##..

print(next(basket)) # [prints A]

print("=========")
## GENERATOR

def square(limit):
  x = 0
  while x < limit:
    yield x * x
    yield x * x * x
    x += 1

sqaure_and_cuber = square(10)
print(next(sqaure_and_cuber), "print 0 ** 2")
print(next(sqaure_and_cuber), "print 0 ** 3")
print(next(sqaure_and_cuber), "print 1 ** 2")
print(next(sqaure_and_cuber), "print 1 ** 3")
print(next(sqaure_and_cuber), "print 2 ** 2")
print(next(sqaure_and_cuber), "print 2 ** 3")
