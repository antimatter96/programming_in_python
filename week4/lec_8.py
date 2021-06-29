# Matrix Multiplication - 1

## C[i][j] = row[i] of A * col[j] * B

## C[row][col]

for k in len(A[0]):
  C[row][col] += A[row][k] * B[k][col]
