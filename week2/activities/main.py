import calendar
import math
import random

# Q1
a = 1
print(type(a))
a = 1.
print(type(a))
a = '1'
print(type(a))

# Q2
# output => true
x, y, z = 3, 4, 5
x, y, z = x**2, y**2, z**2
print(x+y == z)

# Q3
# no error
# no error
# no error
# error
# error
# error

# Q4
# swaps
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)

# Q5
# => No

# Q6
# Similar
x = True
if x:
  print("Works 1")
if x == True:
  print("Works 2")

# Q7
# position of else
# second check not needed
x = input()
if x%10 == 0:
  print("10")
elif x%5 == 0:
  print("5")
else:
  print("None")

# Q8
# print leap/non leap year

# Q9
# no check for positive
# no check for a+b>c
# missed one check in isoceles

# Q10
x = int(input())
if x%2==0:
  print("Even")
else:
  print("Odd")

# Q11
x = int(input())
if x%10 == 9:
  print("")
elif x%10 == 8:
  print("")
elif x%10 == 7:
  print("")
elif x%10 == 6:
  print("")
elif x%10 == 5:
  print("")
elif x%10 == 4:
  print("")
elif x%10 == 3:
  print("")
elif x%10 == 2:
  print("")
elif x%10 == 1:
  print("")
else:
  print("Zero")

# Q12
a,b,c = int(input()),int(input()),int(input())
if a+b==c or b+c==a or c+a==b:
  print("good triplet")

# Q13
a,b,c = int(input()),int(input()),int(input())
if a + b<c and b+c < a and c+a < b:
  print("True => triangle possible")

# Q14
a,b,c,d = int(input()),int(input()),int(input()), int(input())
if a <= b <= c <= d:
  print("asc")
else:
  print("not asc")

# Q15
print(calendar.day_name[calendar.weekday(1996, 6, 6)])

# Q16
enc = 'udymts'
alpha = 'abcdefghijklmnopqrstuvwxyz'
t = ''
shift = -5
t = t + alpha[ (alpha.index(enc[0]) + shift)%26 ]
t = t + alpha[ (alpha.index(enc[1]) + shift)%26 ]
t = t + alpha[ (alpha.index(enc[2]) + shift)%26 ]
t = t + alpha[ (alpha.index(enc[3]) + shift)%26 ]
t = t + alpha[ (alpha.index(enc[4]) + shift)%26 ]
t = t + alpha[ (alpha.index(enc[5]) + shift)%26 ]
# => python

# Q17
e = ''
if e:
  print("Not empty")
else
  print("Empty")

zero = 0
if zero:
  print("if zero is true")
else:
  print("false")

## empty string -> false
## 0 -> false, +ve, -ve -> true

# Q18
# int vs float
print(2**5, type(2**5))
print(math.pow(2,5), type(math.pow(2, 5)))

# Q19
# => 2
print("A")
print("\n")
print("B")

# Q20
num = str(input())
first_digit = int(str[0])
second_digit = int(str[1])
third_digit = int(str[2])
if third_digit - first_digit == second_digit or third_digit - first_digit == -second_digit:
  print("sandwich")
else:
  print("plain")

# Q21
message = 'Txt me when u receive this msg.'
message = message.replace("Txt", "Text")
message = message.replace("u", "you")
message = message.replace("msg", "message")

# Q22
s = str(input())
print(s.count(' ') + 1)

# Q23
s = str(input())
print(s.count('.'))

# Q24
s = str(input())
s.replace('O', '0')

# Q25
s = str(3 ** 100)
print("0", s.count('0'))
print("1", s.count('1'))
print("2", s.count('2'))
print("3", s.count('3'))
print("4", s.count('4'))
print("5", s.count('5'))
print("6", s.count('6'))
print("7", s.count('7'))
print("8", s.count('8'))
print("9", s.count('9'))

# Q26
# => 2
s = '''1
2
3'''
print('\n' in s)
print(s.count('\n'))

# Q27
x = float(input())
print( 1.0 / (1 + pow(math.e, -x)) )

# Q28
s = "ABCDEF"
print(s.find("Z"))
print(s.index("Z"))

## find returns -1
## index throws error

# Q29
a = "#something#"
b = "_something_"

print((a in b) or (b in a))
print((a in b) or (a not in b))

# Depends
# Always true

# Q30
HT = 'ht'
print(random.choice(HT))

# => chooses a random from given array/string

# Q31
alpha = "ABCDEFGH"
s = str(input())
x_1, y_1 = str(s[0]), int(s[1])
x_2, y_2 = str(s[3]), int(s[4])

x_1_index = alpha.find(x_1)
x_2_index = alpha.find(x_2)

if abs(x_1_index - x_2_index) == abs(y_1 - y_2):
  print("YES")
else:
  print("NO")


###
### => abs
###

# Q32
x = int(input())
if x <= 1:
  print("No")
elif x%2 == 0:
  print("Yes")
else:
  print("No")

# Q33
s = str(input())
print("length", len(s))
print("wins", s.count("W"))
print("3 game win", "WWW" in s)
print("first win", s.index("W"))

# Q34
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = str(input())
col = 0
if len(s) > 1:
  col += (alpha.index(s[0])+1) * 26

col += (1 + alpha.index(s[-1]))
print(col)

# Q35
s = str(input)
if s.isalpha():
  print("valid")
else:
  print("invalid")
