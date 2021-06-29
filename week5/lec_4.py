# Matrix multiplication

# Matrix Multiplication - 2

## C[i][j] = row[i] of A * col[j] * B

# C[row][col]
# for k in len(A[0]):
#   C[row][col] += A[row][k] * B[k][col]

r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A = [r1, r2, r3]
B = [s1, s2, s3]

N = 3

C = [[0,0,0], [0,0,0], [0,0,0]]

for row in range(len(A)):
    for col in range(len(B[0])):
        ## C[row][col] = row[row] of A * col[col] * B
        for k in range(len(A[0])): #len(B)
            C[row][col] += A[row][k] * B[k][col]

print(C)

# import numpy

# X = numpy.mat(A)
# Y = numpy.mat(B)

# print(X * Y)

def init_matrix(m , n, fill):
  A = []
  for i in range(m):
    l = []
    for j in range(n):
      l.append(fill)
    A.append(l)
  return A

def row(A, i):
  l = []
  for k in range(len(A[0])):
    l.append(A[i][k])
  return l

def col(A, j):
  l = []
  for k in range(len(A)):
    l.append(A[k][j])
  return l

def scaler_multiplication(A, B):
  sum = 0
  for i in range(len(A)):
    sum += A[i] * B[i]
  return sum

def vector_multiplication(A, B):
  m = len(A)
  n = len(B[0])
  C = init_matrix(m, n, 0)

  for i in range(m):
    for j in range(n):
      C[i][j] = scaler_multiplication( row(A, i) , col(B, j) )

  ## init_max(m, n)
  ## C[i][j] = row[i] of A * col[j] of B
  return C

print(A, B)
print(vector_multiplication(A, B))

X = [[1, 2, 3]]
Y = [[1], [2], [3]]
print(vector_multiplication(X, Y))
print(vector_multiplication(Y, X))
