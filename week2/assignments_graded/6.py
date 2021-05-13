s = str(input())

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

banned = '''\/='" '''

if len(s) < 8 or len(s) > 32:
    print("False")
elif lower.count(s[0]) == 0 and upper.count(s[0]) == 0:
    print("False")
else:
    if '\\' in s or '/' in s or ' ' in s or '\"' in s or '\'' in s:
        print("False")
    else:
        print("True")
