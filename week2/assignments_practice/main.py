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
