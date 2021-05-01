a = int(5.7)
## b = int("5.7") breaks
c = int("5")
d = int(-5.7)

print(a, type(a))
## print(b, type(b))
print(c, type(c))
print(d, type(d))

a = float(5)
b = float("5.7")
c = float("5")
d = float("5.0")


print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a = str(0)
b = str(0.0)
c = str(-0.0)
d = str(-0)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a = bool(5)
b = bool(-5)
c = bool(5.0)
d = bool(-5.0)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a = bool(0)
b = bool(-0)
c = bool(0.0)
d = bool(-0.0)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a = bool("0")
b = bool("hello")
c = bool("True")
d = bool("False")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a = bool("")
b = bool(" ")

print(a, type(a))
print(b, type(b))
