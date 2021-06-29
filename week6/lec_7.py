# More on sets

st = {1,2,3,4,5}
print(st)

st.add(1)
print(st)

# iunordered
# st[0] -> NO , not subscriptable

# set is mutable
# values have to be immutable => dicts which are only hashable


A = {1,2,3,4}
B = {0,1,2,3,4,5}

print(A.issubset(B))
print(A.issubset(B))

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)
