# 

def is_folder(path:str):
  return not is_file(path)

def is_file(path:str):
  return is_code(path) or is_image(path)

def is_code(path:str):
  split = path.split('.')
  if len(split) == 1:
    return False
  ext = split[1]
  return ext == "py" or ext == "cpp"

def is_image(path:str):
  split = path.split('.')
  if len(split) == 1:
    return False
  ext = split[1]
  return ext == "jpg" or ext == "png"

def level(path:str):
  return path.count('/')

s1 = "/home/mark/facebook/src/newsfeed.py"
s2 = "/home/guido/microsoft/secret/mystery/src"
s3 = "/home/einstein/relativity.jpg"

for s in [s1, s2, s3]:
  print(is_folder(s))
  print(is_file(s))
  print(is_code(s))
  print(is_image(s))
  print(level(s))
