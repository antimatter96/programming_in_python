# string
# lower
# print in asc order

s = str(input())
s = s.lower()
s = list(s)
s.sort()
ans = ''
for c in s:
  if c.isalpha():
    ans += c
print(ans)
