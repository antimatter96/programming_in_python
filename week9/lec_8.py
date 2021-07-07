# Pandas 2

import pandas as pd

scores = pd.read_csv("../Datasets/scores_dataset.csv")
# scores => Dataframe, 2D structure / Table
# column => series

print(type(scores))
print(type(scores["Total"]))

# print top 5 rows
print(scores.head())

# print last 5 rows
print(scores.tail())

# specific row
ss = scores[scores["Name"] == "Nisha"]
print(scores[scores["Name"] == "Nisha"])
print(type(ss))    # also datframe

# topper marks based on gender
# all male
print(scores[scores["Gender"] == 'M'])
# total column
print(scores[scores["Gender"] == 'M']['Total'])
# max
print(scores[scores["Gender"] == 'M']['Total'].max())

print(scores[scores["Gender"] == 'F']['Total'].max())

## group by
print(scores.groupby("Gender").max("Physics"))

# categorise based on marks physics

print(scores[scores["Physics"] > 85])
print(scores[scores["Physics"].between(70, 85)])
print(scores[scores["Physics"].between(60, 70)])
print(scores[scores["Physics"] < 60])

print(scores[scores["Physics"] > 85].shape[0])
print(scores[scores["Physics"].between(70, 85)].shape[0])
print(scores[scores["Physics"].between(60, 70)].shape[0])
print(scores[scores["Physics"] < 60].shape[0])

#
print(scores[(scores["Gender"] == 'F') & (scores["Physics"] > 85)])
print(scores[(scores["Gender"] == 'M') & (scores["Physics"] > 85)])

#
subjects = ["Mathematics", "Physics", "Chemistry"]
for sub in subjects:
  print("Abpve 85", sub)
  print(scores[(scores["Gender"] == 'F') & (scores[sub] > 85)])
  print(scores[(scores["Gender"] == 'M') & (scores[sub] > 85)])

# above aberage

for sub in subjects:
  print("Abpve avg", sub)
  avg = scores[sub].mean()
  print(scores[(scores["Gender"] == 'F') & (scores[sub] > avg)])
  print(scores[(scores["Gender"] == 'M') & (scores[sub] > avg)])

# group by

# gives pandas indices as list of dict
# { 'M' => [0,1], 'F' => [2, 4]}
print(scores.groupby('Gender').groups)
print(scores.groupby('CityTown').groups)

for sub in subjects:
  print("Abpve avg", sub)
  avg = scores[sub].mean()
  print(scores[scores[sub] > avg].groupby("Gender").groups)

for i in scores:
  print(i, "<")


print(scores["Total"][0])
