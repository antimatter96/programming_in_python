# nested for loop

s = 'VIBGYOR'

print(s[0])
print(s[1])
print(s[2])

for i in range(len(s)):
  print(s[i])

count = 0
for i in range(len(s)):
  for j in range(len(s)):
    print(s[i], s[j])
    count+=1

print(count)
