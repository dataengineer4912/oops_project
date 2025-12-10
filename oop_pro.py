from Register import RegisterSystem
from login import LoginSystem
class NLPApp:
    def __init__(Self):
        Self.database={}
        Self.first_menu()

    def first_menu(self):
        first_input=input("""
                        Hi! How would you like to proced?
                          1. Not a member? Register
                          2. Alreday Member? Login
                          3. Exist
                          """)
        
        if first_input == '1':
            self.register()

        elif first_input == '2':
            self.login()

        else:
            exit()

    

    def register(self):
        reg=RegisterSystem(self.database)
        reg.register()
        self.first_menu()

    def login(self):
        log=LoginSystem(self.database)
        log.login()
        self.first_menu()

 

obj = NLPApp()   