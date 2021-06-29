# sort then search

def min_in_list(l):
  minimun = l[0]
  for e in l:
    if e < minimun:
      minimun = e
  return minimun

def simple_sort(l):
  sorted_list = []
  while len(l) > 0:
    minimum = min_in_list(l)
    l.remove(minimum)
    sorted_list.append(minimum)

  return sorted_list

s1 = simple_sort([1,2,3,5,8,9])
s2 = simple_sort([8,7,5,1,2,2,0])

def simple_search(l, k):
  if len(l) == 0:
    return False

  mid = (0 + len(l)-1)//2

  if len(l) > 1:
    if l[mid] == k:
      return True

  if len(l) == 1:
    if l[mid] == k:
      return True
    else:
      return False

  if k > l[mid]:
    return simple_search(l[mid+1:], k)
  elif k < l[mid]:
    return simple_search(l[:mid-1], k)

print(simple_search(s1, 1))
print(simple_search(s1, -1))
print(simple_search(s1, 0))
print(simple_search(s1, 10))
