# Matplotlib

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.array([1,2,3,4,5,1,2,3,4,5])
y = np.array([
  100,112,123,123,143,
  134,122,92,120, 80]
)

print(x.__len__())
print(y.__len__())

plt.scatter(x, y)

x = np.array([5,4,3,2,1,1,2,3,4,5])
y = np.array([100,112,123,123,143,134,122,92,120, 80])

# np.random.shuffle(x)
# np.random.shuffle(y)
plt.scatter(x, y)

# plt.show()

labels = np.array(["A", "B", "C"])
vals = np.array([1,2,1])

plt.barh(labels, vals)
# plt.show()

plt.bar(labels, vals)
# plt.show()


x = np.random.normal(10, 2, 20)

plt.hist(x)
# plt.show()

#
plt.pie(vals, labels=labels, startangle=90)
# plt.show()

####
# subplot

size = 500
x = np.array(range(1, size + 1))
y = np.random.normal(100, 1, size)

plt.subplot(2,3,1)
plt.plot(x,y)

## no of cols, no of rows
# where ith plot will go

for i in range(2, 7):
  x = np.random.normal(range(1, size + 1))
  y = np.random.normal(100, i ** 2, size)

  plt.subplot(2,3,i)
  plt.plot(x,y)

plt.show()

# 1 2 3
# 4 5 6
