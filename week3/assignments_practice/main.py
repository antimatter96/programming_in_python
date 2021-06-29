s = "abcdefghijklmnopqrstuvwxyz"
a = 1
b = 3
c = 26
d = 26
e = 0
print("a",s[-a:-26:-3])
print("b",s[::-b])
print("c",s[c:0:-3])
print("d",s[26:-d:-3])
print("e",s[:e:-3])



## Do while loop

for i in range (10,0,1):
  print("AA")
## => no print, if end < small, step should be < 0

# [1231, -12420)
for i in range(1231, -12420, -7):
  print(i)
