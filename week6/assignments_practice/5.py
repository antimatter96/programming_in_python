#

"""
| Description                                     | Set Symbol         | Count of Students     |
|-------------------------------------------------|--------------------|-----------------------|
| played a                                        | a                  | n(a)                  |
| played b                                        | b                  | n(b)                  |
| played c                                        | c                  | n(c)                  |

| played both a and b                             | a_and_b            | n(a_and_b)            |
| played both b and c                             | a_and_c            | n(a_and_b)            |
| played both a and c                             | b_and_c            | n(b_and_c)            |

| played a and b and c                            | a_and_b_and_c      | n(a_and_b_and_c)      |
| played any three sports (a set of all students) | a_or_b_or_c        | n(a_or_b_or_c)        |

| played only a and b not c                       | only_a_and_b_not_c | n(only_a_and_b_not_c) |
| played only a and c not b                       | only_a_and_c_not_b | n(only_a_and_c_not_b) |
| played only b and c not a                       | only_b_and_c_not_a | n(only_b_and_c_not_a) |

| played only a                                   | only_a             | n(only_a)             |
| played only b                                   | only_b             | n(only_b)             |
| played only c                                   | only_c             | n(only_c)             |
"""

s1="1,4,7,10"
s2="1,3,5,7,9,10"
s3="1,2,4,6,8,10"

a = set(s1.split(","))
b = set(s2.split(","))
c = set(s3.split(","))

total = len(a | b | c)

n_a = len(a)
n_b = len(b)
n_c = len(c)

def pprint(a:int, b:float):
  print("{},{:.1f}".format(a, b))

pprint(n_a, n_a/total)
pprint(n_b, n_b/total)
pprint(n_c, n_c/total)

n_a_and_b = len(a & b)
n_b_and_c = len(b & c)
n_b_and_a = len(c & a)

pprint(n_a_and_b,n_a_and_b/total)
pprint(n_b_and_c,n_b_and_c/total)
pprint(n_b_and_a,n_b_and_a/total)

a_and_b_and_c = (a & b & c)
n_a_and_b_and_c = len(a_and_b_and_c)
pprint(n_a_and_b_and_c, n_a_and_b_and_c/total)

n_a_or_b_or_c = len(a | b | c)
pprint(n_a_or_b_or_c, n_a_or_b_or_c/total)

n_a_and_b_not_c = len( (a & b ).difference(a_and_b_and_c) )
n_b_and_c_not_a = len( (b & c ).difference(a_and_b_and_c) )
n_c_and_a_not_b = len( (c & a ).difference(a_and_b_and_c) )

pprint(n_a_and_b_not_c, n_a_and_b_not_c/total)
pprint(n_c_and_a_not_b, n_c_and_a_not_b/total)
pprint(n_b_and_c_not_a, n_b_and_c_not_a/total)

n_only_a = len( a.difference(b | c) )
n_only_b = len( b.difference(c | a) )
n_only_c = len( c.difference(a | b) )

pprint(n_only_a, n_only_a/total)
pprint(n_only_b, n_only_b/total)
pprint(n_only_c, n_only_c/total)
