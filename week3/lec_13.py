# break
# exit loop

# accept email, print username part ie till @
email = str(input())
for c in email:
  if c == '@':
    break
  print(c, end='')
print()

# print in diff lines, usernME, DOMAINS
for c in email:
  if c == '@':
    print()
    continue
  print(c, end='')
print()
# continue => skip to next value, finding nearest loop

# pass
# print all div by 3

# pass => noop;
for x in range(1, 10+1):
  if x%3==0:
    print(x)
  else:
    pass

# else cannot be empty
