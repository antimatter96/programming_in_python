# FUNCTIONAL

# LAMBDA FUNCTION
# ANONYMOUS

def add(x, y):
  return x + y
def sub(x, y):
  return x - y

## OR

add_new = lambda x, y : x+y
sub_new = lambda x, y : x-y


print(type(add))
print(type(add_new))

print(add(10, 10))
print(add_new(10, 10))
print(add_new(8,8))
## ENUMARATOR

fruits = ["a", "b", "c", "d", "e", "f", "a"]
size = ["1", "2", "3", "44", "5", "1", "9"]

for fruit in fruits:
  print(fruit)
  # 'a'
  # 'b'


for i in range(len(fruits)):
  print(i, fruits[i])
  # int, value in list
  # have to make sure they match

for fruit in enumerate(fruits):
  print(fruit)
  # (0, 'a')
  # (1, 'b')

print(zip(fruits, size))

print(list(zip(fruits, size)))
print(dict(zip(fruits, size)))

##### 

a = [10,20,30,40,50,60, 111]
b = [5,10,15,20,25,30]
## c = a - b ## FAILS

def sub(x, y):
  return x-y

c = map(sub, a, b)
print(list(c))

def fnyshit(x):
  return x * x

c = map(fnyshit, a)
print(list(c))

# if more than one list given => will do it till shortest list

##

import math

a = [25, -16, 9, 81, -100]
def square_root(n):
  return math.sqrt(n)

c = map(square_root, a) # this wont throw error
#print(list(c)) # this will

## Filter

def is_positive(n):
  if n >= 0:
    return n
c = map(square_root, filter(is_positive, a))
print(list(c))
