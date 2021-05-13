# more

# Keywords
# and or if

# only alphnumnric with underscores
# can't start with number
# case sensitive

# multiple assignment
x, y = 1, 2
print(x, y)

x = y = z = 10
print(x, y, z)

x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)

# delete
x = 10
del x
print(x)

# => will throw not defined error

# shorthand operators

count = 0
count = count + 1  # OR
count += 1

# => easier to read
# => smaller to type

count -= 1
count *= 2
count /= 2

# in
# search in

print("Alpha" in "asd salphas is a a")
print("Alpha" in "asd sAlphas is a a")


# chaining

x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < (x*10) < 100)
print(10 > x <= 9)
print(5 == x > 4)

# all possible should be true
