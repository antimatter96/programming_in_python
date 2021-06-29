# More on Lists

l1 = [1,2,3]
l2 = ['A', 'B', 'C']
l12 = l1 + l2
l21 = l2 + l1
print(l12)
print(l21)

l1 = [0,0,0,0,0,0]
print(l1)

l1 = [0] * 12
print(l1)

## WRONG
m = 3
n = 3
l1 = [0] * m
l2 = [l1] * n
print(l2)
l2[0][0] = 12
print(l2) 

####

l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
print(l1 == l2)
print(l2 == l3)
print(l1 > l3)
#==
print([1,2] < [2,2])
print([] < [2])
print([] < [-1])

# compare element wise -> if same throughout, compare length

#==============

# can update list in place
# mutable
# strings can't be => no item assignemnt, immutable

l = [1,2,3]
l[0] = 3

#==
x = 10 # allot memory, store 10 in it, name it x
y = x # craetes another memory location, stores value of x in it, name it y
## 2 memory locations are known
x = 5 # replace value at memory location x
print(x, "= 5", y, "= 10")

l1 = [1,2,3] # allots memory, stores these values, names it x
l2 = l1 # no new allocation => add one more name for memory location
## 1 memory location
l1[0] = 123 # updates value in mem location
print(l1, l2, "are same")

## deep copy
l2 = list(l1)

l3 = l1[:]

l4 = l1.copy()

l5 = l1

print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)

#===
l1 = [1]
s = "1"
x = 1

def add(x):
  x = x + 1

def replace(s):
  s = "B"

def app(l):
  l.append(2)
  l += [3]
  print(l is l1, "TRUE")
  l = l + [4] ### wont reflect on existing
  print(l is l1, "FALSE")

add(x)
replace(s)
app(l1)
print(x)
print(s)
print(l)

# mutable are passed by reference
# single version, no copy

###
print(l)
l.insert(2, 9)
print(l)

l.pop()
print(l)
l.pop(2)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)
