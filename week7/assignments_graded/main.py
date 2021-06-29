arr = [
  ("a", "b"),
  ("a", "c"),
  ("a", "d"),
  ("a", "e"),
]

for x,y in arr:
  print(x, y)

d = {}

d.update([("Q", "B")])
print(d)
d.update({"A" : "A"})
print(d)
d.update([arr[3]])
print(d)

##

a = 10
b = 20
def v(a):
  return(a + w(b, a))

def w(a, b = 1):
  a+=b
  return(a)

def x(a = 1, b= 1):
  a+=b
  return(a)

def y(a = 1):
  global b
  a+=b
  b+=1
  return(a)

def z(a):
  if a:
    a += z(a-1)
  return a

print(v(a), a, b)
print(w(a), a, b)

print(y(a), a, b)
a = 10
b = 20
y(a)
print(z(a),a, b)

M = [[1,2,3],[4,5,6]]
def doSomething(M, r, c):
  print(len(M) * len(M[0]))
  if len(M)*len(M[0]) == r*c:
    l= []
    for i in M:
      for j in i:
        l.append(j)

    M_ = []

    for i in range(r):
      M_.append([])
      for j in range(c):
        M_[-1].append(l.pop(0))
    return M_

print(doSomething(M, 2, 3))

print(doSomething(M, 1, 6))
print(doSomething(M, 6, 1))

x = "A BV CVs D 44.73 asd/asd asd."
y = "B"
z = "C"
s = [x,y,z]
print(s)
s = [x] + [y] + [z]
print(s)
print(x.split())
print(x.split(" ")[::2])

for i in [0,1,2]:
  print(i)
