# problem 1
## even or odd

'''
x = int(input("Enter number : "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

### 4 -> Even
### 5 -> Odd
### 0 -> Even
### -7 -> Odd
### -10 -> Eve

# problem 2
## number ends with 0 or 5 or any other number
'''
x = int(input("Enter number : "))
if x % 10 == 0:
    print("0")
elif x % 10 == 5:
    print("5")
else:
    print("Other")
'''
### 20 -> 0
### 14 -> Other
### 5 -> 5
### 0 -> 0
### -27 -> Other
### -10 -> 0

# problem 3
# Assign grades
## A => x >= 90
## B => 80 <= x < 90
## C => 70 <= x < 80
## D => 60 <= x < 70
## E => x < 60


x = int(input("Enter marks : "))

'''
if x > 100 or x < 0:
    print("Invalid Input")
elif x >= 90:
    print("A")
elif 80 <= x < 90:
    print("B")
elif 70 <= x < 80:
    print("C")
elif 60 <= x < 70:
    print("D")
else:
    print("E")
'''

'''
if x > 100 or x < 0:
    print("Invalid Input")
elif x >= 90:
    print("A")
elif x >= 80
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("E")
'''
### 95 -> A
### 87 -> B
### 70 -> C
### 62 -> D
### 0 -> E
### 100 -> A
### -5 -> Invalid Input
### 110 -> Invalid Input


###########
'''
ELSE IF
=> If earlier was false and this is true
'''
###########

# problem 4
# flowchart to code

print("Travel from A to B")
time = int(input("Enter time : "))
time_condition = int(input("What is time limit : "))

price = int(input("Enter price : "))
price_condition = int(input("What is price limit : "))

if time ?= time_condition:
    if price >= price_condition:
        print("Train")
    else:
        print("Coach")
else:
    if price >= price_condition:
        print("Daytime Flight")
    else:
        print("Red eye flight")
