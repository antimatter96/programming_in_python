#

# x = int(input())
# i = 0
# while x %10**i != x:
#   print(i)
#   i = i+1

j = 0
for i in range(1231, -12420, -7):
  j = j+1
print(j)

x = 0
for i in range(10):
  for j in range(10):
    x+=1
    break
  x+=1
  break
print(x)

for i in range(10, 0, 1):
  print(i)

x = 0
x_ = 1
for i in range(10):
  x, x_ = x_, x + x_
print(x)

x = 0
x_ = 1
for i in range(10):
  x = x_
  x_ = x + x_
print(x)

print("AB\n"*10, sep='\n')
