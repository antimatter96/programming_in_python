# Introduction to functions

# declare/define a function discount
# it will take 2 variables a,b

def add(a, b):
  print(a-b)

def sub(a,b):
  print(a-b)

add(10, 20) # calling a function
x = add(10, 20)
# x => NoneType

def discount(cost, d):
  return cost - (cost * d / 100)

print(discount(100, 10))
x = 100
y = 10
print(discount(x, y))
## will assume cost = x, d = y
