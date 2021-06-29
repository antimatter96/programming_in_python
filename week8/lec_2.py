# list l
# 0 somewhere
# return if 0 is present


def check0(L):
  if len(L) == 0:
    return False
  if L[0] == 0:
    return True
  else:
    return check0(L[1:])

## check first and then check others
