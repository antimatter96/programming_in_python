#

import math
from os import kill


obj1 = {1: 40, 2: 39, 3: 20, 4: 33, 5: 36}
"""
1
5
3
1
[(1, 40), (2, 39), (3, 20), (4, 33), (5, 36)]
[(5, 36), (4, 33), (3, 20), (2, 39), (1, 40)]
[(3, 20), (4, 33), (5, 36), (2, 39), (1, 40)]
[(1, 40), (2, 39), (5, 36), (4, 33), (3, 20)]
"""

obj2 = {4: 40, 5: 39, 3: 20, 6: 33, 2: 36}
"""
2
6
3
4
[(2, 36), (3, 20), (4, 40), (5, 39), (6, 33)]
[(6, 33), (5, 39), (4, 40), (3, 20), (2, 36)]
[(3, 20), (6, 33), (2, 36), (5, 39), (4, 40)]
[(4, 40), (5, 39}, (2, 36}, (6, 33), (3, 20)]
"""


def min_dict_key(data:object):
  keys = list(data.keys())
  keys.sort()
  return keys[0]


def max_dict_key(data:object):
  keys = list(data.keys())
  keys.sort(reverse=True)
  return keys[0]
  pass


def min_value_dict_key(data:object):
  min_value = math.inf
  min_value_key = None

  for key in data:
    if data[key] < min_value:
      min_value_key = key
      min_value = data[key]
  
  return min_value_key


def max_value_dict_key(data:object):
  max_value = -math.inf
  max_value_key = None

  for key in data:
    if data[key] > max_value:
      max_value_key = key
      max_value = data[key]

  return max_value_key


def sort_by_key(data:object, order="asc"):
  keys = list(data.keys())
  keys.sort()
  if order == "desc":
    keys.reverse()
  output = []
  for key in keys:
    output.append( (key, data[key]) )
  return output

def value(ele:tuple):
  return ele[1]

def sort_by_value(data:object, order="asc"):
  sort_order = order == "desc"
  l = list(data.items())
  l.sort(key=value, reverse=sort_order)

  return l


print(min_dict_key(obj1))
print(max_dict_key(obj1))
print(min_value_dict_key(obj1))
print(max_value_dict_key(obj1))
print(sort_by_key(obj1, order="desc"))
print(sort_by_value(obj1, order="desc"))
