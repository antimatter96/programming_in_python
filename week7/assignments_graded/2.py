# students

TEST_CASE = str(input())

n = int(input())

cols = str(input()).split(",")
students = {}
for i in range(n):
  x = {}
  inp = str(input()).split(",")
  id = int(inp[0])
  students[id] = x
  for i in range(1, len(cols)):
    x[cols[i]] = int(inp[i])
