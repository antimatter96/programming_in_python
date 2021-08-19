# Inheritance and method overriding

# adding more qulaities
# change exsiting beahviour 

class Student():
  def __init__(self, name, age, marks) -> None:
    self.name = name
    self.age = age

    self.marks = marks

  def display(self):
    print(self.name, self.age, self.marks)

class Employee():
  def __init__(self, name, age, salary) -> None:
    self.name = name
    self.age = age

    self.salary = salary

  def display(self):
    print(self.name, self.age, self.salary)

# Avoid duplication by using inheritance
# common qualties of parent

#############

# every student IS A person
# every employee IS A person

class Person():
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class StudentNew(Person):
  def __init__(self, name, age, marks) -> None:
    super().__init__(name, age) ##
    self.marks = marks

  def display(self):
    super().display()
    print(self.marks)

class EmployeeNew(Person):
  def __init__(self, name, age, salary) -> None:
    super().__init__(name, age) ##
    self.salary = salary

  ## overriding
  def display(self):
    print(self.name, self.age, self.salary)

s1 =  StudentNew("Arpit", 23, 199)
s1.display()

## 4/5 types of inheritenace

# simple
# parent -> child class
# one parent, one child

# hieraichial
# parent -> child class 1
#        -> child class 2
# one parent, multiple child

# multiple inheritance
# parent 1
#        -> child class
# parent 2

# multilevel inheritance
# parent -> intermediate [behaves as child of parent, parent of child] -> child

# hyrbid
# -> mix and match

