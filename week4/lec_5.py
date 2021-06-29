# Obvious Sort => Selection

l = [7, 12, 10, 7, 18, 6, 42, 8, 35, 7]

# Find least element

# find least element in l
# remove from l
# append in x
x = []

# min = l[0]
# for i in range(len(l)):
#   if min > l[i]:
#     min = l[i]
# print(min)
# x.append(min)
# l.remove(min)


while len(l) > 0:
  min = l[0]
  for i in range(len(l)):
    if min > l[i]:
      min = l[i]
  x.append(min)
  l.remove(min)
print(l)
print(x)
