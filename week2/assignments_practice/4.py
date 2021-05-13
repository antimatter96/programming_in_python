s = str(input())
if len(s)%2 == 0:
  if s[-1] == '.':
    s = s[0:len(s)-1]
  else:
    s = s + '.'
middle = int(len(s)/2)
ans = s[middle-1:middle+2]
print(ans)
