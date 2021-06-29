# solve equations

def solve(eq1, eq2):
  a1, b1, c1 = eq1
  a2, b2, c2 = eq2

  x = -((c1 * b2) - (c2 * b1))/((a1 * b2) - (a2 * b1))
  y = ((c1 * a2) - (c2 * a1))/((a1 * b2) - (a2 * b1))

  return int(x), int(y)

eq1 = [1, -2, 6]
eq2 = [3, 5, -15]
print(solve(eq1, eq2))

eq1 = [10, -4, -58]
eq2 = [6, 4, 10]
print(solve(eq1, eq2))
