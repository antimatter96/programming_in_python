# tutorial

# print all prime numbers less than entered
# n = int(input())

# for i in range(3, n):
#   prime = True
#   for j in range(2, i):
#     if i%j == 0:
#       prime = False
#       break
#   if prime:
#     print(i, end=' ')

## accept trader till "-1"
## for each trader accept p/l till 0

# trader_id = str(input())
# while trader_id != '-1':
#     s = 0
#     p_l = int(input())
#     while p_l != 0:
#         s += p_l
#         p_l = int(input())

#     print(s)
#     trader_id = str(input())

## accept no of days
## for each day accept heighths till -1, print sum

# days = int(input())
# for i in range(days):
#     s = 0
#     p_l = int(input())
#     while p_l != -1:
#         s += p_l
#         p_l = int(input())

#     print(s)

# find word of longest word entered till "-1"
max = 0
inp = str(input())
while inp != "-1":
  if max < len(inp):
    max = len(inp)

  inp = str(input())

print(max)
