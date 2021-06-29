# Dot Product

l = [1, 3, 4, 67, 18, 17]
sum = 0
for e in l:
    sum += e
print(sum)

sum = 0
for i in range(len(l)):
    sum += l[i]
print(sum)

# To find dot product of two vectors
x = [1, 7, 3, 4]
y = [8, 6, 3, 2]

if len(x) != len(y):
  print("NOT OF SAME SIZE")

dot_product = 1*8 + 7*6 + 3*3 + 4*2

sum = 0
for i in range(len(x)):
    sum += (x[i] * y[i])

print(dot_product, sum)
