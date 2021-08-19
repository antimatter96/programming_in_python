# Functional 2

# INLINE STATEMENTS

a = 10
b = 20
if a < b:
  small = a
else:
  small = b

print(small)

## OR

small = a if a < b else b

print(small)

#

a = 5
while a > 0:
  print(a)
  a -= 1

## OR

a = 5
while a > 0: print(a); a-=1

## NO PERFORMANCE IMPACTS

## ====

# LIST COMPREHENSTION

fruits = ["aa", "ab", "ac", "bb"]
new_list = []
for fruit in fruits:
  if 'b' in fruit:
    new_list.append(fruit.capitalize())

## OR

new_list = [fruit.capitalize() for fruit in fruits if 'b' in fruit]
