# Pearson correlation coefficient

import math

def mean(l):
  sum = 0
  for e in l:
    sum += e
  return sum/len(l)

def scalar_multiply(l1, l2):
  sum = 0
  for i in range(len(l1)):
    sum += l1[i] * l2[i]
  return sum

def pearson_correlation(x, y):
  if len(x) != len(y):
    return 0.0
  x_bar = mean(x)
  y_bar = mean(y)

  x_diff = []
  y_diff = []

  for i in range(len(x)):
    x_diff.append(x[i] - x_bar)
    y_diff.append(y[i] - y_bar)

  num = scalar_multiply(x_diff, y_diff)

  den = 1
  den *= math.sqrt( scalar_multiply(x_diff, x_diff) )
  den *= math.sqrt( scalar_multiply(y_diff, y_diff) )

  return round(num/den, 1)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 2, 3, 4, 3, 4, 5]

print(pearson_correlation(x, y))

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
y = [-1.0, -2.0, -3.0, -4.0, -5.0, -1.0, -2.0, -3.0, -4.0, -5.0]

print(pearson_correlation(x, y))
