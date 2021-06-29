# warmup

# check if k is in list l

def obvious_seach(l:list[int], k:int):
  for e in l:
    if e == k:
      return 1
  return 0

# how long someting takes

def sum(n):
  '''Retuns sum of first n'''
  ans = 0
  for i in range(n):
    ans = ans + i
  return ans

import time
limt = 100
a=time.time();print(sum(limt));b=time.time()
print(b - a)
a=time.time();print(sum(limt * 10));b=time.time()
print(b - a)
a=time.time();print(sum(limt * 100));b=time.time()
print(b - a)

#======================
# int(10/3) == 10//3
#======================

l = [0,1,2,3,4,5,6,7,8,9]
begin = 0
end = 9

mid_point = (begin + end)//2 # starting from begin, ending at end indexes
# 3,4,5
mid_point = ( 4 + 6 )//2

##
##  import file_name
## 
## file_name.function_name
## 

limt = 1000000
l1 = range(limt)
l2 = range(limt * 10)
l3 = range(limt * 100)
a=time.time();print(obvious_seach(l1, 1122200));b=time.time()
print(b - a)
a=time.time();print(obvious_seach(l2, 11222000));b=time.time()
print(b - a)
a=time.time();print(obvious_seach(l3, 112220000));b=time.time()
print(b - a)

## for obvious_search the nearer to start, the faster
## time is more for element not in list or at end
