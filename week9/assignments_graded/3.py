def solution():
  '''
    1. Process version_1.txt and version_2.txt
    2. Print the number lines in version_2.txt that are not in version_1.txt
    '''
  f = open("version_1.txt", "r")
  g = open("version_2.txt", "r")

  lines1 = list()
  line = f.readline().strip()
  while line:
    lines1.append(line)
    line = f.readline().strip()

  lines2 = list()
  line = g.readline().strip()
  while line:
    lines2.append(line)
    line = g.readline().strip()

  count = 0
  for x in lines2:
    if x == '':
      continue
    if x not in lines1:
      count = count + 1

  return count


print(solution())
