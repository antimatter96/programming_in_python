# Birthday Paradox

import random

# print(random.random())
# print(random.randint(0, 1))
# randint => [a, b]

days = []
no_of_students = 100
for i in range(no_of_students):
    days.append(random.randint(1, 365))

days.sort()
duplicate = False
duplicates = []
i = 0
while i < len(days)-1:
    if days[i] == days[i+1]:
        duplicate = True
        count = 2
        while i < len(days)-2 and days[i+1] == days[i+2]:
          i+=1
          count+=1
        duplicates.append([days[i], count])
    i += 1
print(days)
print(duplicate, duplicates)

#####

# MAX_NO_OF_STUDENTS = 60
# NO_OF_OBS = 5000
# for no_of_students in range(10, MAX_NO_OF_STUDENTS+1):
#     positive = 0
#     for _i in range(NO_OF_OBS):
#         days = []
#         for i in range(no_of_students):
#             days.append(random.randint(1, 365))

#         days.sort()
#         duplicate = False
#         duplicates = []
#         i = 0
#         while i < len(days)-1:
#             if days[i] == days[i+1]:
#                 duplicate = True
#                 break
#             i+=1

#         if duplicate:
#             positive += 1
#     print(f"{no_of_students} => {positive/NO_OF_OBS * 100}")
