# print digits as words
n = int(input())

digits = list(str(n))

mapping = {
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
}

for digit in digits:
  print(mapping[digit])

s = ''
s += mapping[digits[0]]
for i in range(1, len(digits)):
  s += mapping[digits[i]].title()
print(s)
