class father:
    def funA(self):
        print("This function is in the parent class.")
# Derived class 
class mother(father): 
    def funB(self):
        print("This function is in class child_one.")
# Derived class 
class child(mother):
    def funC(self):
        print("This function is in class child_two.")
