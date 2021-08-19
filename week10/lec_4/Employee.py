from Person import Person

class Employee(Person):
  def __init__(self, name, age, salary) -> None:
    super().__init__(name, age) ##
    self.salary = salary

  ## overriding
  def display(self):
    print(self.name, self.age, self.salary)
