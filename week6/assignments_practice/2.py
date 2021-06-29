# transpose

data = [{
    'Roll': [1, 2, 3]
}, {
    'Name': ['A', 'B', 'C']
}, {
    'Course': ['X', 'Y', 'Z']
}]


def table_to_record(table_db):
  output = []
  length = 0
  col_names = []

  for col_data in table_db:
    col_name = ''
    for e in col_data:
      col_name = e

    col_names.append(col_name)
    length = len(col_data[col_name])

  for i in range(length):
    data = {}
    for col_name in col_names:
      data[col_name] = None
    output.append(data)

  for col_data in table_db:
    col_name = ''
    for e in col_data:
      col_name = e

    for i in range(length):
      output[i][col_name] = col_data[col_name][i]

  return output


print(table_to_record(data))
