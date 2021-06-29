# while to compute factorial

n = int(input())

# ans = 1
# ans = ans * 2
# ans = ans * 3

i = 1
ans = 1
while(i <= n):
  ans = ans*i
  i = i+1

print(ans)
