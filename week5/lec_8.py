# Scope

# Call by value
# only passing value to function
# not passing the variable
# just passing the value
# not for list

# Global and Local Variables

x = 5 # GLOBAL
def func2(x): ## this x is not the same as above
  x = x + 3
  print(x)
  # this x is scoped only to this function

print(x)

func2(x)

print(x)

def func3():
  x += 3 ## WILL THROW ERROR, WHAT IS X
func3()
print(x)

def func3():
  global x # there is a global varible x, looks for it, doesnt create a copy of it, refers to global in this function
  x += 3
func3()
print(x)

def func3(x):
  # global x # WILL THROW ERROR
  x += 3
func3()
print(x)


k = 4
def f():
  print(k, "<<")
  ## WILL TRY TO FIND IN OUTER SCOPE



l = [1,2,3]
def fun(x):
  x.append(0)
fun(l)
print(l)

