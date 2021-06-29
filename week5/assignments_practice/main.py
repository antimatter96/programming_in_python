l1 = [1,2,3,4,5,6,7,8,9]
l1[0:2] = [10,20,30,40,50]

print(l1)

l1 = [1,2,3,4,5,6,7,8,9]
l1[0:1] = [10]
print(l1)

l2 = [1,2,3,4,5,6,7,8,9]
l2[0] = [10]
print(l2)


l1 = [1,2,3,4,5]
l2 = [6,7,8,9]

newlist = l1 + l2
print(newlist)

newlist = l1.extend(l2)
print(newlist)

l1.extend(l2)
print(l1)
