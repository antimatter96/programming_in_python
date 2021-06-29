# are parenthesis mathced , max_depth
s = str(input())
matched = True
cnt = 0
max_depth = 0
for e in s:
    if e == '(':
        cnt+=1
        if max_depth < cnt:
            max_depth = cnt
    elif e == ')':
        cnt-=1
    if cnt < 0:
        matched = False
if cnt ==0 and matched:
    print(max_depth)
else:
    print("Not matched")
