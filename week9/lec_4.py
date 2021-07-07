# Very big files

f = open("file.txt", "r")
# does not load the whole into memory
s = f.readline()
f.close()
# goes line by line


#######

# f.read() => whole file as a string

f = open("file.txt", 'r')
file = f.read()
print(file)
f.close()

#######

# f.readline() => reads a line, including the '\n' if present
# gives '' at the end

f = open("file.txt", 'r')
line = f.readline()
while line != '':
  print(line)
  line = f.readline()
f.close()

f = open("file.txt", 'r')
line = f.readline()
while line != '':
  print(line, end='')
  line = f.readline()
f.close()

## '' is treated as False
f = open("file.txt", 'r')
line = f.readline()
while line:
  print(line.strip())
  line = f.readline()
f.close()

## f.readlines => reads all lines as a list, each has '\n' if present
f = open("file.txt", 'r')
lines = f.readlines()
while line:
  print(line.strip())
f.close()

## f.write() writes a string as is

## f.writeline()

f = open("writing.txt", 'w')
f.write(str(1))
f.close()

f = open("writing.txt", 'w')
f.writelines(["A", "B", "C"])
# writes ABC
f.close()

