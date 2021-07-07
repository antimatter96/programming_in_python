#

f = open('mytext.txt', 'w')
f.write("Hello")
f.write("I am Arpit")
f.write('\n')
f.write('Second Line')
f.close()

""""
HelloI am Arpit
Second Line
"""

# wont write until close() is callled

# open a text file ---- in writing mode

# mode 'a' => append
x = open('mytext.txt', 'r')
s = x.read()
print(s)
print(len(s))
print(s.count('\n'))
## s.close()
