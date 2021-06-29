# tutorialß

##
# fact
# n = int(input())
# if n >= 0:
#   fact = 1
#   while(n > 0):
#     fact *= n
#     n = n-1
#   print(fact)
# else:
#   print("UNDEF")


##
# number of digits in a number
# n = int(input())
# if n < 0:
#   n = 0-n

# i = 1
# while(n > 9):
#   i = i+1
#   n = n//10

# print(i)

##
# reverse
# n = int(input())
# wasNegative = False
# if n < 0:
#   wasNegative = True
#   n = 0-n

# i = 0
# while(n > 0):
#   i = i * 10
#   i += n%10
#   n = n//10

# if wasNegative:
#   i = 0-i

# print(i)

##
# if palindrome or not
inp = int(input())
n = abs(inp)
if n < 0:
  n = 0-n

i = 0
while(n > 0):
  i = i * 10
  i += n%10
  n = n//10

if inp < 0:
  i = 0-i

print(i == inp)
