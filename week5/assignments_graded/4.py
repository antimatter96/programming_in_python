# magic square
def is_magic(mat):
    n = len(mat)
    d1_sum = 0
    d2_sum = 0
    for i in range(n):
      d1_sum += mat[i][i]
      d2_sum += mat[i][n-i-1]
    if d1_sum != d2_sum:
      return "NO"

    row_sums = []
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += mat[i][j]
        row_sums.append(row_sum)

    for i in range(n-1):
      if row_sums[i] != row_sums[i+1]:
        return "NO"

    col_sums = []
    for i in range(n):
        col_sum = 0
        for j in range(n):
            col_sum += mat[j][i]
        col_sums.append(col_sum)

    for i in range(n-1):
      if col_sums[i] != col_sums[i+1]:
        return "NO"
    
    if col_sums[0] != row_sums[0] or col_sums[0] != d1_sum or row_sums[0] != d1_sum:
      return "NO"

    return "YES"




mat1 = [[1, 2], [2, 1]]
mat2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

print(is_magic(mat1))
print(is_magic(mat2))
