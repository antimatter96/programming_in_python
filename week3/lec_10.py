# tutorial

#
# fact
n = int(input())
if n >= 0:
  fact = 1
  while(n > 0):
    fact *= n
    n = n-1
  print(fact)
else:
  print("UNDEF")

n = int(input())
if n >= 0:
  fact = 1
  for i in range(n, 1, -1):
    fact = fact * i
  print(fact)
else:
  print("UNDEF")

# which to use
# do we know range?
# Yes: for loop
# No : while loop

# number of digits in a number
n = int(input())
if n < 0:
  n = 0-n

i = 0
for c in str(n):
  i+=1
print(i)

# reverse
n = int(input())
wasNegative = False
if n < 0:
  wasNegative = True
  n = 0-n

i = ''
for c in str(n):
  i = c + i
if wasNegative:
  print(-i)
else:
  print(i)

# palindrome
n = int(input())
if n < 0:
  n = 0-n

i = ''
for c in str(n):
  i = c + i

print(i == str(n))

# accept integers until something
# while loop

# multipliacation
# for

# prime or not
# for

# sum of all digits
# while

# find numbers less than n, dividsible by 3 or 5
# for

# print factors
# for
