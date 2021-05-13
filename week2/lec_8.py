## if statement

print("Enter doy")
birth_year = int(input())

current_year = 2021

age = current_year - birth_year
print(age)

if age < 13:
  print("Cant watch")
  print("Try again next year")
else:
  print("WATCH")
  print("BUY POPCORN")

print("END")
