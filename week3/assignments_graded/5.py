# Accept phone number from user as string.

# A valid phone number should satisfy the following constraints.

# 2. Length of the number should be 10.
# 1. The number should start with 6,7,8 and 9.
# 3. Number should not have any digit repeated more then 5 times in consecutive manner.
# 4. Number should not have any digit more than 7 times.

s = str(input())
if len(s) != 10:
    print("invalid")
else:
    if not s.isdecimal():
        print("invalid")
    else:
        if int(s[0]) < 6:
            print("invalid")
        else:
            count = 1
            max_count = -1
            for i in range(1, 10):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    if count > max_count:
                        max_count = count
                    count = 1
            if count > max_count:
                max_count = count
            if max_count > 5:
                print("invalid")
            else:
                count = 1
                max_count = -1
                s_copy = list(s)
                s_copy.sort()
                s = ''
                for c in s_copy:
                    s += c
                for i in range(1, 10):
                    if s[i] == s[i-1]:
                        count += 1
                    else:
                        if count > max_count:
                            max_count = count
                        count = 1
                if count > max_count:
                    max_count = count
                if max_count > 7:
                    print("invalid")
                else:
                    print("valid")
