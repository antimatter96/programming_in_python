class Person():
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
    self.__wont__inherit # private members
    ## all others are public

  def display(self):
    print(self.name, self.age)
