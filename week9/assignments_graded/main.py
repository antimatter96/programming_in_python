##
f = open("nums.txt", 'r')
nums = list()
line = f.readline().strip()
while line != '':
  nums.append(int(line))
  line = f.readline().strip()
print(len(nums))
print(type(f))
print(f.readline() == '')
print(f.readline() == line)

f.close()

x = "asd\n"
f = open("file.txt", "w")
for i in range(10):
  f.write(x)
f.close()

##########

# Code -1
f = open('nums.txt', 'r')
l1 = []
text = f.read()
while '\n' in text:
  index = text.find('\n')
  l1.append(text[:index])
  text = text[index+1:]
f.close()

# Code-2	
f = open('nums.txt', 'r')
l2 = f.readlines()
f.close()

# 
f = open('nums.txt', 'r')
l3 = []
while True:
  text = f.readline()
  if text == '':
    break
  l3.append(text)
f.close()

print(len(l1))
print(len(l2))
print(len(l3))
