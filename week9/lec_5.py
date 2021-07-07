# ceaser cipher
# shift letters by 3 units

# create intitial dictionary

from io import TextIOWrapper
import string

def create_ceaser_dictionary(x:int=3):
  dic = {}
  l = list(string.ascii_lowercase)

  for i in range(len(l)):
    dic[l[i]] = l[ (i+x) % 26]

  return dic

def encrypt(input_file_name, output_file_name):
  cipher = create_ceaser_dictionary(-3)

  f = open(input_file_name, 'r')
  g = open(output_file_name, 'w')

  replace_file_characters(f, g, cipher)


def decrypt(input_file_name, output_file_name):
  cipher = create_ceaser_dictionary(-3)

  f = open(input_file_name, 'r')
  g = open(output_file_name, 'w')

  replace_file_characters(f, g, cipher)


def replace_file_characters(input_file:TextIOWrapper, output_file:TextIOWrapper, cipher:dict):
  c = input_file.read(1)
  while c != '':
    if c in cipher:
      output_file.write( cipher[c] )
    else:
      output_file.write(c)
    c = input_file.read(1)


########################

