# process

def process():
  while True:
    a = board_min()
    board_erase(a)
    if board_isEmpty():
      return a
    b = board_min()
    board_erase(b)

    board_write(abs(a-b))
