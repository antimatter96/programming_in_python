# transpose

def transpose(mat):
  m = len(mat)
  n = len(mat[0])

  C = []
  for i in range(n):
    temp = []
    for j in range(m):
      temp.append(0)
    C.append(temp)

  for i in range(m):
    for j in range(n):
      C[j][i] = mat[i][j]

  return C

mat = [
  [1, 2],
  [3, 4],
  [5, 6],
]

transpose(mat)

mat = [
  [1, 2, 3 ,4],
  [5, 6, 7, 8],
]

transpose(mat)
