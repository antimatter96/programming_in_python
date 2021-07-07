# Big text file handling

# find a number in this file

# approach one
f = open('file.txt', 'r')

s = ""

flag = 0
while(s != ''):
  s = f.readline()
  if s!='':
    n = int(s) # phone numbers

    if n == 123123123:
      print("found")
      flag = 1
      break

if flag == 0:
  print("Not found")

f.close()
## OR

# prints
# asd
#
# asd
#
f = open("file.txt", 'r')
for line in f:
  print(line)
f.close()

# prints
# asd
# asd
f = open("file.txt", 'r')
for line in f:
  print(line, end='') ## print asd\n
f.close()
