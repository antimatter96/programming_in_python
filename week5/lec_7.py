# Function arguments


# func def
# func call
# func arguments
# func parameters
# func body

# Sequence matters
# POSITIONAL ARGUEMNTS
def func1(a,b,c):
  print("a", "=>", a)
  print("b", "=>", b)
  print("c", "=>", c)
func1("a", "b", "c")

#KEYWORD ARGUEMNRS
func1(a= "a", b= "b", c="c")
func1(c= "c", a= "a", b="b")

#DEFAULT ARGUMENTS
def func1(a,b = "b",c = "c"):
  print("a", "=>", a)
  print("b", "=>", b)
  print("c", "=>", c)
func1("a")
func1("a", "b")
# IF arg not present => default

func1("a", c = "c")

# POSITIONAL FIRST THEN KEYWORD


## DEFAULT RETURN IS None
