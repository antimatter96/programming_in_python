# Matrix Addition

r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A = [r1, r2, r3]
B = [s1, s2, s3]

print(A, B)
N = 3
# create C with all 0

C = [[0,0,0], [0,0,0], [0,0,0]]
# C = [[], [], []] => Not defined
for i in range(N):
  for j in range(N):
    C[i][j] = A[i][j] + B[i][j]

print(C)

######

r1=[1,2,3,4]
r2=[4,5,6,7]
r3=[7,8,9,14]
r4 = [1,1,2,2]

s1=[1,2,1,2]
s2=[6,2,3,15]
s3=[4,2,1,45]
s4=[1,7,2,9,9]

A = [r1, r2, r3, r4]
B = [s1, s2, s3, s4]

print(A, B)
N = 4
# create C with all 0

C = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
# C = [[], [], []] => Not defined
for i in range(N):
  for j in range(N):
    C[i][j] = A[i][j] + B[i][j]

print(C)
