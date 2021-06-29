#

subject_topics = [
  [ "list", "functions", "variables", "booleans", "list", "exceptions", "conditions", "input", "loops"],
  ["strings", "variables", "input", "exceptions", "integers", "booleans", "loops"],
  ["algorithm", "variables", "complexity", "tree", "stack", "queue"],
  ["join", "floats", "integers", "constraints", "aggregate", "select", "where"]
]

def num_of_occurences(subject_topics, topic):
  n = 0
  for s in subject_topics:
    if topic in s:
      n = n + 1
      continue
  return n

def trending(subject_topics):
  subject_topics_set_flat = set()

  for e in subject_topics:
    subject_topics_set_flat = subject_topics_set_flat.union(set(e))

  max_occ = 0
  max_occ_count = 0
  min_occ = 99999999999
  min_occ_count = 0

  for topic in subject_topics_set_flat:
    occ = num_of_occurences(subject_topics, topic)

    if occ > max_occ:
      max_occ = occ
      max_occ_count = 1
    elif occ == max_occ:
      max_occ_count += 1
    
    if occ < min_occ:
      min_occ = occ
      min_occ_count = 1
    elif occ == min_occ:
      min_occ_count += 1

  return (max_occ_count, min_occ_count)

print(trending(subject_topics))
