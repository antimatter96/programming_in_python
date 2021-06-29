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

import numpy

X = numpy.mat(A)
Y = numpy.mat(B)

print(X * Y)
