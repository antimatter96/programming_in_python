import math

# Q1
# int, float, string, boolean, list

# Q2
# email address -> string
# annual income -> float
# number of days in a month -> int

# Q3


# Q4
ans = str(7 ** 35)
lastDigit = ans[-1]
print("Q4", "=>", lastDigit)

# Q5
rem = 987654321 % 123456789
print("Q5", "=>", rem)


# Q6
print("Q6", "2")
print("Q6", "8")
print("Q6", "2")
print("Q6", "8")
print("Q6", "2")
# print(5 - 3)
# print(5 - - 3)
# print(5 - - - 3)
# print(5 - - - - 3)
# print(5 - - - - - 3)

# Q7
# 2**2-2-2/2
print("Q7", (2**(2-2))-(2/2))

# Q8
# 0 == 0 < 1 < 2 < 3 > 2 > 1 > 0 == 0
print("Q8", True)

# Q9
# len(s) => n
# len(n * s)
print("Q9", "n * n")

# Q10
# x, y strings
# len(x) + len(y) == len(x + y)
# simple concatenate
print("Q10", True)

# Q11
# print(input())
print("Q11", "Syntactically correct",
      "Waits for users input", "Prints whatever user inputs")

# Q12
# print(input() + input() + input())
# Multiple options
print("Q12", "Multiple Options")
print("Q12", "ENTER 1 ENTER 23", "ENTER")
print("Q12", "ENTER ENTER 123", "ENTER")
print("Q12", "ENTER 1 ENTER 23", "ENTER")
print("Q12", "1 ENTER ENTER 23", "ENTER")
print("Q12", "1 ENTER 23 ENTER", "ENTER")
print("Q12", "123 ENTER ENTER", "ENTER")

# Q13
print("Q13", math.sqrt(12345678987654321))

# Q14
ans = str(7 ** 100)
no_of_digits = len(ans)
print("Q14", no_of_digits)

# Q15
inp = str(input())
print("Q15", inp[0] == inp[len(inp)-1])

# Q16
# inp * 10
x = int(input())
print("Q16", x + x + x + x + x + x + x + x + x + x)

# Q17
# l, b
l = float(input("Enter length"))
b = float(input("Enter breadth"))
print("Q17", l * b


# Q18
# print(float(input()) * float(input()) * float(input()))
print("Q18", "Accept 3 numbers and print thier product)

# Q19
# x = int(input())
# 1.23
print("Q19", "Error => We did not enter a valid int")

# Q20
# print greatest integer less than x
print("Q20", int(float(input())//1))

# Q21
# print smallest integer less than x
print("Q21", int(-(-float(input())//1)))


# Q22
# accept score, print if score [90, 100]
score = float(input())
print("Q22", score >= 90 and score <= 100)

# Q23
# a,b inegers AND b - a == 1 AND 0< a, b < 10
# b = [2,3,4,5,6,7,8,9]
print("Q23", 8)

# Q24
num = str(input())
print("Q24", int(num[0]) + int(num[1]))

# Q25
x = int(input())
sqrt = int(math.sqrt(x))
print("Q25", (sqrt * sqrt) == x)
