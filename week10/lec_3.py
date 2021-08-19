# Attributes and Methods

class Student:
  count = 0
  ## __init__ is the constructor
  ## can take variables
  ## called explicitly
  ## must provide params if defaults are not given

  ## self -> indicates the object itself
  ## container which holds the current object

  ## Since every object has its own copy -> copy them to self.variable
  ## if inside __init__ object owns copy,
  ## else there will be only one copy, owned by the class
  def __init__(self, roll_no, name, total) -> None:
    self.roll_no = roll_no
    self.name = name
    self.total = total


  def display(self):
    print(self.roll_no, self.name, self.total)

  def result(self):
    if self.total > 120:
      print("Pass")
    else:
      print("Fail")

s0 = Student(name='Asd', roll_no=10, total=150)
Student.count += 1
s0.display()
s0.result()

s1 = Student(11, "Asdasd", 100)
Student.count += 1
s1.display()
s1.result()

print(Student.count)

# attribues vs behabours

# CALL THEM METHODS

# inside a class -> METHOD
