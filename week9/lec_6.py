# File handling and genetic sequences

f = open("test.txt", 'r')
f.seek(1)
# index [1
print(f.read(2))

# goes back and forth manually

f = open('human.txt', 'r')

seq = f.read() # whole

diab = "ATCTCTC"

print(diab in seq)

# KNUTH MORRIS PRATT ALGO LEARN
