'''
***************
***************
***************
***************
***************
***************
***************
'''
n = int(input())
print("*" * n)
if n > 1:
  lines = int((n - 3)/2)
  for i in range (0, lines):
    s1 = " " * i
    s2 = " " * (lines-i-1)
    print(f"*{s1}*{s2}*{s2}*{s1}*")
  print("*"*n)
  for i in range (0, lines):
    s1 = " " * i
    s2 = " " * (lines-i-1)
    print(f"*{s2}*{s1}*{s1}*{s2}*")
  print("*"*n)

