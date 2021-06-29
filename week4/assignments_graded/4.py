# string
inp = 0
arr = []
while inp != '':
  inp = str(input())
  arr.append(inp)
arr.pop()
m = len(arr)
n = -1
for i in range(0, len(arr)):
    arr[i] = arr[i].split(' ')
    arr[i].reverse()
    n = len(arr[i])
for i in range(0, n):
    for j in range(0, m-1):
        print(arr[j][i], end=' ')
    print(arr[m-1][i])
