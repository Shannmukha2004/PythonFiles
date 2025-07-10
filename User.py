class User:
    def login(self):
        print("Login Successful")
class BussinessUser(User):
    def run_add(self):
        print("Add Successful")
b=BussinessUser()
b.login()
b.run_add()
