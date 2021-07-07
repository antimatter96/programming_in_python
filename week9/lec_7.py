# Pandas

# import pandas as pd

# csv
# comma seperated values

f = open('../Datasets/scores_dataset.csv', 'r')
data = f.readlines() # read whole file, split by line
#print(data)

max_score = 0
## data[0] is heading
for record in data[1:]:
  fields = record.split(',')
  total = int(fields[8])
  if max_score < total:
    max_score = total
print(max_score)
f.close()

import pandas as pd

scores = pd.read_csv("../Datasets/scores_dataset.csv")
print(scores["Total"].max())

print(scores) ## prints as form of a table
# adds index number automatically

print(scores.shape) # rows * cols
print(scores.count()) # values per col
print(scores["Total"].min())
print(scores["Total"].mean())
print(scores["Total"].median())
print(scores["Total"].sum())
print(scores["Total"].quantile(.90))
print(scores["Total"].sort_values())
print(scores["Total"].sort_values(ascending=False))



