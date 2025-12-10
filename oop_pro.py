
class NLPApp:
    def __init__(Self):
        Self.__database={}
        Self.__first_menu()

    def __first_menu(self):
        first_input=input("""
                        Hi! How would you like to proced?
                          1. Not a member? Register
                          2. Alreday Member? Login
                          3. Exist
                          """)
        
        if first_input == '1':
            self.__register()

        elif first_input == '2':
            self.__login()

        else:
            exit()

    

    def __register(self):
        print("register")
        pass

    def __login(self):
        print("login")  
        pass  

from Register import NLPApp

obj = NLPApp()   