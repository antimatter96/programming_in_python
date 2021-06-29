# user score
def user_score(read_count, reply_count, new_post_count):
  sum = 0
  sum += (1 * read_count)
  sum += (3 * reply_count)
  sum += (5 * new_post_count)
  if sum > 50:
    return "Leader"
  else:
    return "Basic"
