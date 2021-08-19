# binary search -> recursion

def rec_binary_search(l:list[int],k:int, begin, end):
  if end >= len(l):
    print("end out")
    return 0

  if begin < 0:
    print("begin out")
    return 0

  if begin > end:
    print("begin > end")
    return 0

  # 2 or more elements
  mid_point = (end+begin)//2
  if k < l[mid_point]:
    end = mid_point-1

  if k > l[mid_point]:
    begin = mid_point+1

  if k == l[mid_point]:
    return 1

  return rec_binary_search(l, k, begin, end)



def rec_binary_search_2(l:list[int],k:int, begin, end):
  ## find half of list where element might help
  ## search in that half

  if begin > end:
    return 0

  if end >= len(l):
    return 0

  if begin < 0:
    return 0

  if begin == end:
    if k == l[end]:
      return 1
    else:
      return 0

  if end - begin == 1:
    if k == l[end] or k == l[begin]:
      return 1
    else:
      return 0

  # 2 or more elements
  mid_point = (end+begin)//2
  if k < l[mid_point]:
    end = mid_point-1

  if k > l[mid_point]:
    begin = mid_point+1

  if k == l[mid_point]:
    return 1

  return rec_binary_search(l, k, begin, end)


def binary_search(l, k):
  return rec_binary_search(l, k, 0, len(l)-1)

def binary_search_2(l, k):
  return rec_binary_search_2(l, k, 0, len(l)-1)


for i in range(-2, 102):
  if binary_search(range(100000000), i) != binary_search_2(range(100000000), i):
    print("ERROR")


#===============
# Recursion depth is limited
# will not always work
