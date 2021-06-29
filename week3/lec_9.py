# Formatted printing

for x in range(10):
    print(x)

# by default is \n
for x in range(10):
    print(x, end=' ')
print("on same line")
print("on diff line")

d = 10
m = 5
y = 2021
# by default is ' '
print("Date is", d,m,y, sep='/')

print("Date is", end=' ')
print(d,m,y, sep='/')

# fprint
# formatted print

# n = int(input())
n = 3
for i in range(1, 11):
    print(n, "*", i, "=", n*i)

for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')

# print using format
for i in range(1, 11):
    print('{0} * {1} = {2}'.format(n, i, n*i))

# C style / string modulo
for i in range(1, 11):
    print('%d * %d = %d' % (n, i, n*i))

# %d int
# %f float
pi = 22 / 7

print(f'Value of pi = {pi}')
print('Value of pi = {0}'.format(pi))
## C style is restictive
print('Value of pi = %f' % (pi))

pi = 22 / 7

print(f'Value of pi = {pi:.2f}')
print('Value of pi = {0:.2f}'.format(pi))
## C style is restictive
print('Value of pi = %.2f' % (pi))

# .2f => only 2 digits after decimal

print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))

# 5d => write as d, width is 5, right aligned
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))



# "%-ns" 
# beore after a string
# "%ns"
# after a string

print("%-10s" % "Arpit")
print("%10s"% "Arpit")

print("{a} {b}".format(a="AA", b="AA"))
# {x22.2f} : min 22 chars for whole rthing
