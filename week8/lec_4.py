# recursive sort

# min element
# add to front
# add sort rest of the list


def min_in_list(l: list[int]):
  minimum = l[0]
  for e in l:
    if e < minimum:
      minimum = e
  return minimum


def sort_recursive(l: list[int]):
  if len(l) == 0:
    return l
  if len(l) == 1:
    return l
  minimum = min_in_list(l)
  l.remove(minimum)
  return [minimum] + sort_recursive(l)


l1 = [1, 2, 3, 4, 5, 6]
print(sort_recursive(l1))
l1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
print(sort_recursive(l1))
l1 = []
print(sort_recursive(l1))
l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sort_recursive(l1))
