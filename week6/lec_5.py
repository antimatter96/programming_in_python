# More on tuples

# tuple => immutable
# can't modify
# slice possible
# iteraion
# index access

# packing, unpacking

t = 1,2,3
print(type(t))

x,y,z = t
# a,b,c,d = t will error
print(x,y,z)


x = 5
y = 10
x,y = y,x


l = [10]
print(l, type(l))

t = (10)
print(t, type(t))

t = (10,)
print(t, type(t))

t = ([1,2], ['a', 'b'], 3)
#t[0] = [10, 20] # error
t[0][0] = 10
t[0][1] = 20

# can't modify tuples, but can modify tuple elements if they are mutable

# hashable

t = (1,2,3) # hashable
t = ([1,2,3],) # un hashable

# if values in tuple immutable => hashable
# if values in tuple mutable => unhashable
