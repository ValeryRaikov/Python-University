class Person:
    
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def greet_person(self):
        print(f"Hello {self.fname} {self.lname}. Welcome to the system.")
        print(f"This is your personnal information:\nFirst name: {self.fname}\nLast name: {self.lname}\nAge: {self.age}")
        
        
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter yoyr age: "))      
  
person1 = Person(first_name, last_name, age)
person1.greet_person()

class Description(Person):
    
    def __init__(self, fname, lname, age, bio):
        super().__init__(fname, lname, age)
        
        self.bio = bio
        
    def displace_bio(self):
        print(f"This is what you wrote about yourself: {self.bio}")
        
biography = input("Write about yourself: ")
person1 = Description(first_name, last_name, age, biography)
person1.displace_bio()