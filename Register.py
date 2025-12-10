# Register

class RegisterSystem:
    def __init__(self, database):
        self.database = database


    def register(self):
       print("Register!")
       name=input("Enter Name: ") 
       email=input("Enter Email:  ")
       password=input("Enter password: ")

       if email in self.__database:
          print("Email already exist!") 

       else:
          self.database[email]=[name,password]
          print("Registration Successfully. Please Login !")
          print(self.__database) 
          self.first_menu()

    def login(self):
       print("Login!")            

       

