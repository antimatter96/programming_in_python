#string
#print elements in prime indices
s = str(input())
index = 0
for c in s:
    prime = True
    for i in range(2, index):
        if index%i == 0:
            prime = False
            break
    if index > 1 and prime:
        print(c)
    index+=1
