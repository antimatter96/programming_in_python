alpha='abcdefghijklmnopqrstuvwxyz'

print(len(alpha))
i = 25 # 0, 10, 20
print(alpha[i])
# print(alpha[i+1])
# print(alpha[i+2])
# print(alpha[i+3])

# to deal with str index out of range
# => modulo operator

i = 25
print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])

###

s = 'india'
# expect joejb
# shift it by one letter
t = ''

print( alpha[ (alpha.index(s[0])+1)%26] )
t = t + alpha[ (alpha.index(s[0])+1)%26 ]

t = ''
i = 0
t = t + alpha[ (alpha.index(s[i+0])+1)%26 ]
t = t + alpha[ (alpha.index(s[i+1])+1)%26 ]
t = t + alpha[ (alpha.index(s[i+2])+1)%26 ]
t = t + alpha[ (alpha.index(s[i+3])+1)%26 ]
t = t + alpha[ (alpha.index(s[i+4])+1)%26 ]
print(t)

##
t = ''
i = 0
shift = 1
t = t + alpha[ (alpha.index(s[i+0])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+1])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+2])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+3])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+4])+shift)%26 ]
print(t)

##
t = ''
i = 0
shift = 4
t = t + alpha[ (alpha.index(s[i+0])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+1])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+2])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+3])+shift)%26 ]
t = t + alpha[ (alpha.index(s[i+4])+shift)%26 ]
print(t)


##
## IF STRING LENGTH CHANGES => Will have to make code changes
##

# ceaser cipher when k = 3
# decrypt using k = -3

clear='india'
enc = ''
i = 0
shift = 3
enc = enc + alpha[ (alpha.index(clear[i+0])+shift)%26 ]
enc = enc + alpha[ (alpha.index(clear[i+1])+shift)%26 ]
enc = enc + alpha[ (alpha.index(clear[i+2])+shift)%26 ]
enc = enc + alpha[ (alpha.index(clear[i+3])+shift)%26 ]
enc = enc + alpha[ (alpha.index(clear[i+4])+shift)%26 ]
print(enc)

dec = ''
i = 0
shift = -3
dec = dec + alpha[ (alpha.index(enc[i+0])+shift)%26 ]
dec = dec + alpha[ (alpha.index(enc[i+1])+shift)%26 ]
dec = dec + alpha[ (alpha.index(enc[i+2])+shift)%26 ]
dec = dec + alpha[ (alpha.index(enc[i+3])+shift)%26 ]
dec = dec + alpha[ (alpha.index(enc[i+4])+shift)%26 ]
print(dec)
