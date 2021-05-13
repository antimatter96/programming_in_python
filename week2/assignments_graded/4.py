s = str(input())
vowels = ''
if s.count('a') > 0 or s.count('A') > 0:
    vowels = vowels + 'a'
if s.count('e') > 0 or s.count('E') > 0:
    vowels = vowels + 'e'
if s.count('i') > 0 or s.count('I') > 0:
    vowels = vowels + 'i'
if s.count('o') > 0 or s.count('O') > 0:
    vowels = vowels + 'o'
if s.count('u') > 0 or s.count('U') > 0:
    vowels = vowels + 'u'
print(vowels)
