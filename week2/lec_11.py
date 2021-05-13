# diff ways to import

'''
import calendar

print(calendar.month(2021, 1))
print(calendar.calendar(2021))
'''
'''
from calendar import *

print(month(2021, 1))
'''

# import => can only be access using
# wont know about anything inside
# from import => adds specified fucntions of this library to this program

'''
from calendar import month, calendar

print(month(2021, 2))
print(calendar(2021))
print(calendar.calendar(2021))
'''

'''
import calendar as c
print(c.month(2021, 12))
'''


from calendar import month as mon,  calendar as cal
print(mon(2021, 10))
