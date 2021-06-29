# More on dictionaries

d = {'key': 'value'}
print(d['key'])

d[1] = "allowed"
d[1.1] = "allowed"
#d[False] = "allowed"
print(d)
#print(d[True])

#d[ [1,2] ] = 1 # NO UNHASABLE
d[ (1,2) ] = "allowd" # hashable
print(d)
#d[ ([1,2],1) ] = "allows" # NO UNHASHABLE

# any value

# passed as references

for key in d:
  print(key, "==>,", d[key])

print(d.keys())
print(d.values())
print(d.items()) # lost of tuples
