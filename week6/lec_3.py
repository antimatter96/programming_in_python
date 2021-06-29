# Tuples

l = [1,2,3]
l.append(4)
l.remove(2)

s = {1,2,3}
s.add(4)
s.remove(2)

## A TUPLE IS UNCHANGEABLE
## IMMUTABLE
t = (1,2,3)
print(t[0], t[1])


# t is inflexible
t = tuple(range(1,11))
print(t)

# used when we want fixed

import string
t = tuple(list(string.ascii_letters))
s = set(list(string.ascii_letters))
l = list(string.ascii_letters)
print(s, t, l)

x = "asdnkjand909()asd__%734"
r = []
for p in x:
  if p in t:
    r.append(p)
print(r)

## => size is smaller
print(l.__sizeof__())
print(t.__sizeof__())
print(s.__sizeof__())

# when we are sure of the list we are handling, are sure it will never change
from datetime import date, datetime

print()
c = 10000000
t1 = datetime.now()
s = set(range(0, c))
t2 = datetime.now()
print("set took", t2-t1)
t2 = datetime.now()
t = list(range(0, c))
t3 = datetime.now()
print("list took", t3-t2)
t3 = datetime.now()
l = tuple(range(0,c))
t4 = datetime.now()
print("tuple took", t4-t3)

print()

t1 = datetime.now()
x = c + 1 in s
t2 = datetime.now()
print("set took", t2-t1)
t2 = datetime.now()
y = c + 1 in l
t3 = datetime.now()
print("list took", t3-t2)
t3 = datetime.now()
z = c + 1 in t
t4 = datetime.now()
print("tuple took", t4-t3)

print()
print(s.__sizeof__())
print(l.__sizeof__())
print(t.__sizeof__())
