# Find min

def first_element(l):
  return l[0]

def min_list(l):
  minimum = l[0]
  for i in range(0, len(l)):
    if l[i] < minimum:
      minimum = l[i]
  return minimum

def max_list(l):
  maximum = l[0]
  for i in range(0, len(l)):
    if l[i] > maximum:
      maximum = l[i]
  return maximum

print(min_list([1,2,4,6,-1,0]))
print(max_list([1,2,4,6,-1,0]))

"""
  will return a list with all elements of l2 before l1 
"""
def list_prepend(l1, l2):
  l = []
  for i in range(len(l2)):
    l.append(l2[i])
  for i in range(len(l1)):
    l.append(l1[i])
  return l

print(list_prepend(["A", "B"], ["C", "D"]))

"""
  will return a list with all elements of l1 before l2
"""
def list_append(l1, l2):
  l = []
  for i in range(len(l1)):
    l.append(l1[i])
  for i in range(len(l2)):
    l.append(l2[i])
  return l

print(list_append(["A", "B"], ["C", "D"]))


def list_average(l):
  sum = 0
  for i in range(len(l)):
    sum += l[i]
  return sum/len(l)

print(list_average([1,2,3,4,5,6,7]))

# Modular approach to prorgamming
# break problem into piecses
# write pieces as functions
# stitch them together
