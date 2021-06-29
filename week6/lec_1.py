# Sets and Lists

# Tradeoffs between list and sets

# search in l
# e in l
# checks the whole list
# linear search

## [2.71]
## 2.71 in l TRUE
## 2.710 in l TRUE

#### range() => returns a list

s = {1, 2, 3, 7, 8, 8}
print(type(s))
print(s)

print(1 in s)
print(9 in s)

print("=============")
cap = 10000000
l = list(range(cap))
print(0 in l)
print(-1 in l)
# s = set(l)
print("--")
s = set(range(cap)) # will take more time than list
print(0 in s)
print(-1 in l)

# searching in set easier
# sets take more space
# sets not accesible using [] => no order => no first / second element
# set => for membership only
# if we want to use these elements => array


import sys
print(sys.getsizeof(l))
print(sys.getsizeof(s))

# s = {"1", 1}
# l = ["1", 1]
