# matrix

m = int(input())
n = int(input())

matrix = []
for i in range(m):
  row = str(input()).split(" ")
  for j in range(len(row)):
    row[j] = int(row[j])
  if i == 0 or i == m - 1:
    matrix.append(row)
  else:
    modified = [0] * n
    modified[0] = row[0]
    modified[n - 1] = row[n - 1]
    matrix.append(modified)

for row in matrix:
  for i in range(n):
    if i == n-1:
      print(row[i])
    else:
      print(row[i], end=' ')
