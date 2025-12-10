# Login

class LoginSystem:
    def __init__(self, database):
        self.database = database

    def login(self):
        print("Login!")
        email=input("User name/Email")
        password=input("Password")

        if email in self.database:
            if self.database[email][1]==password:
                print("Login Successfully")
            else:
                print("Something is Wrong! Please try again")
                self.login()    
        else:
         print("User is not found!")
         
         