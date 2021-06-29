# Dictionaries

d = {}
d['arpit'] = 12334
d['arpit_2'] = "ads"

print(d)
print(d['arpit'])
# print(d[0]) =>> error

s = """It was Monday morning. Swaminathan was reluctant to open his eyes.
He considered Monday specially unpleasant in the calendar. After the
delicious freedom of Saturday and Sunday, it was difficult to get into the
Monday mood of work and discipline. He shuddered at the very thought of
school: that dismal yellow building; the fire-eyed Vedanayagam, his class teacher; and the headmaster with his thin long cane"""
#s = s.lower()
s = s.replace('\n', " ")
for e in ['.', ',', ':', ';', '\n']:
  s = s.replace(e, "")
malgudi = s.split(' ')
print(len(malgudi))

s =  set(malgudi)
print(len(s))

d = {}
for x in s:
  d[x]=0
print(d)
for x in malgudi:
  d[x]+=1
print(d)

max_freq = 0
max_freq_word = None
for x in d:
  if max_freq < d[x]:
    max_freq = d[x]
    max_freq_word = x
print(max_freq_word, max_freq)


###########

d = {}
for x in s:
  d[x]=0
max_freq = 0
max_freq_word = None
for x in malgudi:
  d[x]+=1
  if max_freq < d[x]:
    max_freq = d[x]
    max_freq_word = x
print(max_freq_word, max_freq)

#============================

# dict values => int, str, dict, list, tuple
