# return freq -> words
malgudi = ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his',
 'eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After',
 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to',
 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at',
 'the', 'very', 'thought', 'of', 'school:', 'the', 'dismal', 'yellow', 'building;', 'the',
 'fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his',
 'thin', 'long', 'cane...']


def get_key(s:str):
  s = s.lower()
  remove = [",", ":", "!", ";", "."]
  for r in remove:
    s = s.replace(r, "")
  return s


def freqWords(words):
  freqDict = {}
  for word in words:
    key = get_key(word)
    if key not in freqDict:
      freqDict[get_key(word)] = 0
    freqDict[get_key(word)]+=1
  reverse = {}
  for cleaned_word in freqDict:
    freq = freqDict[cleaned_word]
    if freq not in reverse:
      reverse[freq] = []
    reverse[freq].append(cleaned_word)
  return reverse

print(freqWords(malgudi))
