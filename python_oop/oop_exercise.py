class Excersise:
    def __init__(self, fname, lname, age, weight, state):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.weight = weight
        self.state = state
        
    def print_info(self):
        print("First name:", self.fname)
        print("Last name:", self.lname)
        print("Age:", self.age)
        print("Weight:", self.weight)
        print("State:", self.state)
        
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
state = input("Describe yourself briefly: ")
        
person = Excersise(fname, lname, age, weight, state)
person.print_info()