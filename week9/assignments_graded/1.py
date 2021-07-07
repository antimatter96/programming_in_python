def solution():
  f = open("WorldPopulation.csv", "r")
  lines = f.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip().split(',')
    if i != 0:
      for j in range(len(lines[i])):
        lines[i][j] = float(lines[i][j])

  population_year = float(input())
  population_threshold = float(input())
  max_field = str(input())

  population_of = 0
  for record in lines[1:]:
    if record[0] == population_year:
      population_of = record[1]

  print(int(population_of))

  min_year = 999999
  for record in lines[1:]:
    if record[1] > population_threshold:
      if min_year > record[0]:
        min_year = record[0]
  print(int(min_year))

  index_of_field = lines[0].index(max_field)
  max_value = 0
  for record in lines[1:]:
    if record[index_of_field] > max_value:
      max_value = record[index_of_field]

  print(max_value)


solution()
