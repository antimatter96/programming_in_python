# list l
# 0 somewhere
# return if 0 is present


def check0(l: list[int]):
  if len(l) == 0:
    return False
  if l[0] == 0:
    return True
  return check0(l[1:])

## check first and then check others
