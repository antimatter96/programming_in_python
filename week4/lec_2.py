# Lists

l = [1, 4, 6, 7]
for e in l[:-1]:
  print(e)

l.append(1024)
print(l)
l.append(1)
print(l)

l.remove(4)
print(l)
l.remove(1)
print(l)

# remove => first occurence

l.remove(1)
print(l)

##########

# Matrix

l = []
l.append(1)
l.append(2)
l.append(3)

t = []
t.append(l)
print(t)
l.append(1123)
print(t)
# t stores reference to l

m = [10, 20, 30]
t.append(m)
print(t)

k = []
k.append(t)
k.append(10)
k.append([1,2,3])
print("k[0]", k[0])
print("",k[1])
print("",k[2])

M = []
M.append([1,2,3])
M.append([4,5,6])
M.append([7,8,9])

print(M[0][1])
print(M[0][0], M[1][1], M[2][2])
