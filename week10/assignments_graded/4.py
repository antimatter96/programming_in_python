class UserLoginInfo():
  def __init__(self, Username, Password=""):
    self.UserName = Username
    self.old_passwords = [Password]

  def RetrievePassword(self):
    return self.old_passwords[-1]

  def ChangePassword(self, New_Password):
    if New_Password in self.old_passwords:
      return "Password already used"

    if len(New_Password) < 7:
      return "Invalid password"

    if not New_Password[0].isupper():
      return "Invalid password"

    if not New_Password.isalnum():
      return "Invalid password"

    self.old_passwords.append(New_Password)
    return "Password updated successfully"

  def Login(self, UserName, Password):
    if self.UserName == UserName and self.old_passwords[-1] == Password:
      return f"Welcome {UserName}"

    return "Username or Password incorrect"

u2 = UserLoginInfo("amit", "Amit456")
a = u2.ChangePassword("123sadas")
b = u2.ChangePassword("_asda45asd")
c = u2.ChangePassword("Asd45")
o = u2.ChangePassword("sadad78#4")
l = u2.ChangePassword("Esadad784")
d = u2.Login("amit", "Amit456")
e = u2.Login("amit", "Amit56")
r = u2.Login("amsadit", "Amit56")
f = u2.RetrievePassword()
y = u2.RetrievePassword()
print(a)
print(b)
print(c)
print(o)
print(l)
print(d)
print(e)
print(r)
print(f)
print(y)

# output :

# Invalid password\n
# Invalid password\n
# Invalid password\n
# Invalid password\n
# Password updated successfully\n
# Username or Password incorrect\n
# Username or Password incorrect\n
# Username or Password incorrect\n
# Esadad784\n
# Esadad784\n

# u1 = UserLoginInfo(input(), input())
# a = u1.ChangePassword(input())
# b = u1.ChangePassword(input())
# c = u1.ChangePassword(input())
# d = u1.Login(input(), input())
# e = u1.Login(input(), input())
# f = u1.RetrievePassword()
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
