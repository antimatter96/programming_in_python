class TimeConverter():

  def __init__(self, time) -> None:
    self.time = time

  def Second_to_Minutes(self):
    t = self.time

    mins = t // 60
    t = t % 60

    secs = t
    return f"{mins:d} min {secs:d} sec"

  def Second_to_Hours(self):
    t = self.time

    hour = self.time // 3600
    t = t % 3600

    mins = t // 60
    t = t % 60

    secs = t
    return f"{hour:d} hr {mins:d} min {secs:d} sec"

  def Second_to_Days(self):
    t = self.time

    days = t // 86400
    t = t % 86400

    hour = t // 3600
    t = t % 3600

    mins = t // 60
    t = t % 60

    secs = t
    return f"{days:d} days {hour:d} hr {mins:d} min {secs:d} sec"


sec = int(input())
a = TimeConverter(sec)
print(a.Second_to_Minutes())
print(a.Second_to_Hours())
print(a.Second_to_Days())
