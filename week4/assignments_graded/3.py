# string
inp = 0
arr = []
while inp != '':
  inp = str(input())
  arr.append(inp)
arr.pop()
for i in range(0, len(arr)):
  arr[i] = int(arr[i])
arr.sort()
for i in range(0, len(arr)):
  for j in range(0, len(arr)):
    if i==j:
      continue
    target = arr[i] + arr[j]
    if target in arr:
      print(arr[i], arr[j])
