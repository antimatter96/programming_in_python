# collatz

def collatz(n):
  if n%2==0:
    return n/2
  else:
    return (3*n) + 1


def collatz_repeat(n:int):
  i = 0
  while n != 1:
    n = collatz(n)
    i+=1
  return i


collatz_repeat(101)
collatz_repeat(100)
collatz_repeat(2463)
collatz_repeat(7)
