#

movies_db = {
    "Avatar": [2_847, 2009],
    "Avengers: Endgame": [2_797, 2019],
    "Titanic": [2_187, 1997],
    "Star Wars: The Force Awakens": [2_068, 2015],
    "Avengers: Infinity War": [2_048, 2018],
    "Jurassic World": [1_671, 2015],
    "The Lion King": [1_656, 2019],
    "The Avengers": [1_518, 2012],
    "Furious 7": [1_516, 2015],
    "Frozen II": [1_450, 2019]
}


def add_movie_to_boxoffice(movies_db, new_movie):
  movies_db.new_movie[0] = [new_movie[1], new_movie[2]]
  return movies_db


def total_collection(movies_db):
  ans = 0
  for k in movies_db:
    ans = ans + movies_db[k][0]
  return ans


def average_collection(movies_db):
  return round(total_collection(movies_db) / (len(movies_db)), 2)


def num_of_movies_above_average_movies(movies_db):
  n = 0
  avg = average_collection(movies_db)
  for k in movies_db:
    if movies_db[k][0] > avg:
      n = n + 1
  return n


def highest_grossing_movie_year(movies_db):
  max_collection = 0
  max_collection_year = 0

  for k in movies_db:
    if movies_db[k][0] > max_collection:
      max_collection = movies_db[k][0]
      max_collection_year = movies_db[k][1]
  return max_collection_year


print(total_collection(movies_db))
print(average_collection(movies_db))
print(num_of_movies_above_average_movies(movies_db))
print(highest_grossing_movie_year(movies_db))
