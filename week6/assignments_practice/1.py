#

# order_list = []


def shift_a_person(order_list: list[int], position):
  if position > len(order_list):
    position = 1
  if position < 1:
    position = 1
  position = position-1
  removed = order_list[position]
  order_list.remove(order_list[position])
  order_list.append(removed)

  order_list.reverse()

  l = []

  s = set()
  for e in order_list:
    if e in s:
      continue
    else:
      l.append(e)
      s.add(e)

  l.reverse()

  return(l)


print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 8, 9], 6))
print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 2, 9], 6))
print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 2, 9], 9))
print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 2, 9], 8))
print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 2, 9], 1))

print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 2, 9], 10))
print(shift_a_person([1, 2, 3, 4,5 ,6, 7, 2, 9], 0))
