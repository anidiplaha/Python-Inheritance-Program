class First:
    def __init__(self):
        self.greet = "Hello"
 

class Second:
    def __init__(self):
        self.name = "George Telegraph"
 

class Child(First, Second):
    def __init__(self):
        First.__init__(self)
        Second.__init__(self)
 
    def combine(self):
        print(self.greet, self.name)
        print("Welcome to GTTI Behala")
 
obj = Child()
obj.combine()
