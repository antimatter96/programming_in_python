import random

# Q1
sum = 0
for i in range(1, 100, 2):
  sum += i
# print(sum)

# Q2
for i in range(2 * 10,0, -2):
# print(i)
  pass

# Q3
# n = int(input())
n = 6
sum = 0
for i in range(1, n+1):
  fact = 1
  number = i
  while number > 1:
    fact = fact*number
    number-=1
  sum += fact
# print(fact/n)

# Q4
# n = int(input())
n = 100
not_prime = []
sum = 0
for i in range(2, n+1):
  prime = True
  for j in range(2, i):
    if i%j == 0:
      prime = False
      break
  if prime == False:
    not_prime.append(i)
# print(len(not_prime), not_prime)

# Q5
# s = str(input())
s = 'qwsdfhus'
vowels = 'aeiou'

not_vowels = []
for c in s:
  if c.lower() in vowels:
    break
  else:
    not_vowels.append(c)
# print(",".join(not_vowels))

# Q6
# start = int(input())
# stop = int(input())
start = 5
stop = 4
if (0 > start or start > 100) or (0 > stop or stop > 100):
  print("Exit")
for i in range(start, stop+1):
  div3 = i % 3 == 0
  div5 = i % 5 == 0
  div10 = i % 10 == 0
  if div3 and div5 and div10:
    break
  elif (div10 and div3) or (div3 and div5) or (div5 and div10):
    pass
  elif div3:
    print("Div by 3")
  elif div5:
    print("Div by 5")
  elif div10:
    print("Div by 10")
  else:
    print(i)

# Q7
# n = int(input())
n = 0
for i in range(1, n+1):
  print(f"Current number is {i:2d} and the cube is {i**3}")

# Q8
if False:
  print("The sum of {}, {} and {} is {}".format(1,2,3,6))
  print("The sum of {0}, {1} and {2} is {3}".format(1,2,3,6))
  print("The sum of {0}, {1} and {c} is {d}".format(1,2,c=3,d=6))
  print("The sum of {a}, {b} and {c} is {d}".format(a=1,b=2,c=3,d=6))

# Q9
# n = int(input())
n = 6
if n < 0:
  print("Exit")
sum = 0
for i in range(1, n+1):
  sum += int("1" * i)
# print(sum/n)

# Q10
# name = input()
# age = input()
name = "Rahul"
age = 21
message="Hii!, I am {}, I am {} year's old".format(name, age)
# print(message)

# Q11
# n = int(input())
n = 1
if n > 10 or n < 1:
  print("Exit")

max_s = (2 * 2 *(n-1)) + 1
for i in range(1, n+1):
  nums = []
  num = n - i + 1
  while num > 1:
    nums.append(str(num))
    num-=1
  nums.append("1")
  num = 2
  while num < n - i + 2:
    nums.append(str(num))
    num+=1
  ss = (" ".join(nums))
  print(ss.center(max_s, " "))

# Q12
# s = str(input())
s = "abbbbbddde"
if len(s) != 10:
  print("EXIT")

current = 1
max = 1
for i in range(1, len(s)):
  if s[i] == s[i-1]:
    current+=1
  else:
    if current > max:
      max = current
    current = 1
if current > max:
  max = current
if max >= 5:
  # print(True)
  pass
else:
  # print(False)
  pass

# Q13
# n = int(input())
n = 5
if n < 0:
  print("Exit")
for i in range(1,n+1):
  for j in range(1, i+1):
    pass
    # print(j, end=' ')
  # print()

# Q14
# s = str(input())
s = "asd"
new = ''
for c in s:
  new = c + new
# print(new)

# Q15
# s = str(input())
s = "asa"
new = ''
for c in s:
  new = c + new
# print(new == s)

# Q16
# s = str(input())
s = "Rohit Sharma"
target = 1
for i in range(1, len(s)):
  if s[i] == ' ':
    target = i + 1
# print(s[0], s[target], sep='')

# Q17
# s = str(input())
s = '|0||0|||0|'
n_zeros = 0
n_pipers = 0
for c in s:
  if c == '0':
    n_zeros+=1
  if c == '|':
    n_pipers+=1
# print("No of boxes", n_pipers-1)
# print("No of empty boxes", n_pipers-1 - n_zeros)
# print("No of boxes with eggs", n_zeros)

# Q18
# s = str(input())
s = 'WLWWWL'
max = 0
current = 0
for c in s:
  if c == 'W':
    current+=1
  else:
    if current > max:
      max = current
    current = 0
if current > max:
  max = current
# print(max)

# Q19
s = -1
l = []
while s!=-1:
  # s = int(input())
  l.append(s)
if len(l) > 0:
  l.pop()
distinct=1
for i in range(1, len(l)):
  if l[i-1]==l[i]:
    pass
  else:
    distinct+=1
# print(distinct)

# Q20
s = -1
l = []
while s!=-1:
  # s = int(input())
  l.append(s)
if len(l) > 0:
  l.pop()
found = -1
asc = True
desc = True
for i in range(1, len(l)):
  if l[i-1] < l[i]:
    desc = False
  elif l[i-1] > l[i]:
    asc = False
if asc:
  # print("asc")
  pass
elif desc:
  # print("desc")
  pass
else:
  pass

# Q21
# n = int(input())
n = -12334
copy = abs(n)
product = 1
while copy > 1:
  # print(copy, copy%10)
  product *= copy%10
  copy = copy//10
# print(product)

# Q22
# a = int(input())
# b = int(input())
a = 12
b = 21

gcd = 1
i = 1
while i < a and i < b:
  if a%i == 0 and b%i==0:
    gcd=i
  i+=1
# print(gcd)

# Q23
# x = int(input())
# n = int(input())
x = 2
n = 4

sum = 0
for i in range(0, n+1):
  sum += x ** i
# print(sum)

# Q24
sum = 0.0
for i in range(1, 100000):
  sum += (1/i)
  if sum >= (1-0.05) * 10:
    # print(i)
    break

# Q25
# n = int(input())
n = 120
den = 1.0
for i in range(2, n+1):
  den += 1/i
# print("{0:.2f}".format(n/den))

# Q26
actual_number = random.randint(1, 100)
guesses = 0
for i in range(0, guesses):
  guess_number = int(input())
  if actual_number - guess_number == 0:
    print("EXCELLENT")
    break
  elif (0 <= actual_number - guess_number <= 10) or (0 <= guess_number - actual_number <= 10):
    print("GOOD")
  elif (guess_number-actual_number > 10):
    print("TOO_HIGH")
  elif (actual_number - guess_number > 10):
    print("TOO_LOW")

# Q27
# n = int(input())
n = 1
a = 1
b = 1
for i in range(2, n):
  a,b = b, a+b
  print(b)

# Q28
# n1 = int(input())
# n2 = int(input())
n1 = 123
n2 = 456

digits_1 = 0
while n1 > 0:
  n1 = n1//10
  digits_1+=1
digits_2 = 0
while n2 > 0:
  n2 = n2//10
  digits_2+=1
# print(digits_1 == digits_2)

# Q29
# n = int(input())
n = 981234
last_digit = n%10
digit = n
while n > 0:
  digit = n%10
  n=n//10
# print(last_digit, digit)
