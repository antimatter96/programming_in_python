class UserLoginInfo():

  UserName = None
  old_passwords = None

  def __init__(self, Username, Password):
    UserLoginInfo.UserName = str(Username)
    UserLoginInfo.old_passwords = [str(Password)]

  def RetrievePassword(self):
    return UserLoginInfo.old_passwords[-1]

  def ChangePassword(self, New_Password):
    New_Password = str(New_Password)

    if New_Password in UserLoginInfo.old_passwords:
      return "Password already used"

    if len(New_Password) < 7:
      return "Invalid password"

    if not New_Password[0].isupper():
      return "Invalid password"

    if not New_Password.isalnum():
      return "Invalid password"

    UserLoginInfo.old_passwords.append(New_Password)
    return "Password updated successfully"

  def Login(self, UserName, Password):
    if UserLoginInfo.UserName == str(
        UserName) and UserLoginInfo.old_passwords[-1] == str(Password):
      return f"Welcome {UserName:s}"

    return "Username or Password incorrect"


u1 = UserLoginInfo(input(), input())
a = u1.ChangePassword(input())
b = u1.ChangePassword(input())
c = u1.ChangePassword(input())
d = u1.Login(input(), input())
e = u1.Login(input(), input())
f = u1.RetrievePassword()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
