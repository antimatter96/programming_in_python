#

# uses json library
# convert an input dictionary string to dictionary object
import json


def add_record(date_table, entity_dict):
  data_table[entity_dict["uid"]] = entity_dict
  return data_table


def search_record(data_table, entity_id):
  if entity_id in data_table:
    return data_table[entity_id]
  return None

def update_record(data_table, entity_id, key, value):
  if entity_id in data_table:
    data_table[entity_id][key] = value

  return data_table


def delete_record(data_table, entity_id):
  data_table.pop(entity_id)

  return data_table


s = """{"uid": 101, "emp_name": "Hari","emp_sal": 100000}"""

entity_dict = json.loads(s)
entity_id = 101

# create a blank dictionary
data_table = {}
# add a record
data_table = add_record(data_table, entity_dict)
print(data_table)
# search a record
print(search_record(data_table, entity_id))
# update a field in the existing record
data_table = update_record(data_table, entity_id,
                           list(data_table[entity_id].keys())[1], "X")
print(data_table)
# delete a record
data_table = delete_record(data_table, entity_id)
print(data_table)
