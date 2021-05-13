a = str(input()) == "True"
b = str(input()) == "True"
c = str(input()) == "True"
print(a,b,c)
if a:
  if b:
    if c:
      print(True)
    else:
      print(False)
  else:
    if c:
      print(True)
    else:
      print(True)
else:
  if b:
    if c:
      print(True)
    else:
      print(False)
  else:
    if c:
      print(True)
    else:
      print(False)
