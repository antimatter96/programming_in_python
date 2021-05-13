name_1, dob_1 = str(input()), str(input())
name_2, dob_2 = str(input()), str(input())
day1, month1, year1 = dob_1[0:0+2], dob_1[3:3+2], dob_1[6:6+4]
day2, month2, year2 = dob_2[0:0+2], dob_2[3:3+2], dob_2[6:6+4]

if year1 < year2:
    print(name_2)
elif year1 > year2:
    print(name_1)
elif month1 < month2:
    print(name_2)
elif month1 > month2:
    print(name_1)
elif day1 < day2:
    print(name_2)
elif day1 > day2:
    print(name_1)
elif name_1 < name_2:
    print(name_1)
else:
    print(name_2)
