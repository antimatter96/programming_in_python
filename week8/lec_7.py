# binary search


def binary_search(l: list[int], k: int):
  """Searches for k in l. l must be sorrted"""

  # [ ...11...   72,81,93 ........]
  # k = 39
  # check mid_point
  # 39 is less than 81
  # 39 must be on the left side of 81
  # can ignore 81 and onwards
  # again check mid_point
  # 39 is more than 11
  # 39 must be on the right side of 11
  # can ignore till 11
  #### list becomes smaller

  ## SORTED -> EASY

  # shrink my list
  # whille loop

  begin = 0
  end = len(l) - 1

  # at least 2 elements
  while end - begin > 1:
    mid_point = (begin + end)//2
    #print("(", end, "+", begin, ")//2 => ", mid_point, "", l[mid_point])

    if k == l[mid_point]:
      return True

    if k < l[mid_point]:
      end = mid_point - 1
      # cut right side
      pass

    if k > l[mid_point]:
      begin = mid_point + 1
      # cut left side
      pass

  #print("(", end, "+", begin, ")//2 => ", mid_point, "", l[mid_point])
  # end - begin <= 1
  # if == 1 => only 2 elements to check
  #print(end - begin)
  if end - begin == 1:
    if k == l[end] or k == l[begin]:
      return True
  if end == begin:
    if k == l[end]:
      return True
  # end == begin ??
  return False

import time
import lec_6

print("------------------------------")
limt = 1000000
l1 = range(limt)
l2 = range(limt * 10)
l3 = range(limt * 100)
a=time.time();print(binary_search(l1, 1122200));b=time.time()
print("binary ", b-a)
a=time.time();print(lec_6.obvious_seach(l1, 1122200));b=time.time()
print("obvious", b-a)
a=time.time();print(binary_search(l2, 11222000));b=time.time()
print("binary ",b-a)
a=time.time();print(lec_6.obvious_seach(l2, 11222000));b=time.time()
print("obvious",b-a)
a=time.time();print(binary_search(l3, 112220000));b=time.time()
print("binary ",b-a)
a=time.time();print(lec_6.obvious_seach(l3, 112220000));b=time.time()
print("obvious",b-a)

