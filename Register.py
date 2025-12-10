# Register

class NLPApp:
    def __init__(self):
        self.__database={}
        self.__first_menu()

    def __first_menu(self):
        first_input = input("""
        Hi! How would you like to proced?
        1.Not a Member? Register
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
       print("Register!")
       name=input("Enter Name: ") 
       email=input("Enter Email:  ")
       password=input("Enter password: ")

       if email in self.__database:
          print("Email already exist!") 

       else:
          self.__database[email]=[name,password]
          print("Registration Successfully. Please Login !")
          print(self.__database) 
          self.__first_menu()

    def __login(self):
       print("Login!")            


obj=NLPApp()       

