# max_element

def max_of_two(a, b):
  if a > b:
    return a
  else:
    return b

def max_element(l):
  if len(l) == 1:
    return l[0]

  if len(l) == 2:
    return max_of_two(l[0], l[1])

  return max_of_two(l[0], max_element(l[1:]))

print(max_element([1,2,3,4]))
print(max_element(["abc", "b", "c","d"]))
