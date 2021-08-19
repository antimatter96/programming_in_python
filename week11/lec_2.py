# Exception Handling

# Exception -> Not really from our end
# Code seems correct

from os import path


a = 1
b = 0
## c = 1/0 WILL GIVE ERROR/EXCEPTIONS
c = "something"

print(c)

## print(d) WILL GIVE ERROR/EXCEPTIONS

## f = open("not exist", 'r') WILL GIVE ERROR/EXCEPTIONS

## HANDLING -> Avoid throwing error, give a deterministic exit
## path

## ==========

try:
  c = a/b
  print(c)
except ZeroDivisionError:
  print("Divisor can not be zero")


try:
  print(d)
except ZeroDivisionError:
  print("Divisor can not be zero")
except NameError:
  print("Variable not defined")

try:
  f = open("asdasdasd", 'r')
except FileNotFoundError:
  print("File does not exist")


try:
  print(d)
except:
  print("Unkown Error")

## WIll check every error one by one, from top to bottom

try:
  print(cd)
  print(1/0)
except ZeroDivisionError:
  print("Divisor can not be zero")
except NameError:
  print("Variable not defined")

try:
  print(1/0)
  print("WONT BE PRINTED")
  print(cd)
except ZeroDivisionError:
  print("Divisor can not be zero")
except NameError:
  print("Variable not defined")

## FINALLY

try:
  f = open("exists", 'r')
  print(asdasd)
except FileNotFoundError:
  print("File does not exist")
except:
    print("Unkwi")
finally:
  f.close()
  print("FINALLT BLOCK")
# Exception in finally block??


a = int(input())
if a < 19:
  print("No")
  raise Exception("You are ubnderage")
  ## USER DEFINED EXCEPTIONS
