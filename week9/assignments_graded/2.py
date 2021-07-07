def highest_grossing(yearFrom, yearUpto, genre):
  '''
    Arguments:
    	yearFrom: int
    	yearUpto: int
    	genre: string
    Returns:
    	movie_name: string
    '''

  gross_index = 9
  year_index = 2

  convert_to_int = [gross_index, year_index]
  f = open("IMDB_reviews.csv", "r")
  lines = f.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip().split(',')
    if i != 0:
      for index in convert_to_int:
        if lines[i][index] != '':
          lines[i][index] = int(lines[i][index])
        else:
          lines[i][index] = 0

  name_index = 1
  genre_index = 4

  max_gross = 0
  max_gross_movie = ''

  for movie in lines[1:]:
    if genre in movie[genre_index] and movie[year_index] >= yearFrom and movie[
        year_index] <= yearUpto:
      if movie[gross_index] > max_gross:
        max_gross_movie = movie[name_index]
        max_gross = movie[gross_index]

  return max_gross_movie


# ###
# import pandas as pd

    # movies = pd.read_csv("IMDB_reviews.csv")
    # i = movies[ (movies["year"] <= 1990) & (movies["year"] >= 1980) & (movies ["genre"] == "Drama")]["gross"].max()
    # print(movies[ movies["gross"] == i ]["name"])

    # i = movies[ (movies["year"] <= 2021) & (movies["year"] >= 2000) & (movies ["genre"] == "Fantasy")]["gross"].max()
    # print(movies[ movies["gross"] == i ]["name"])
