class Person:
    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.naionality = nationality
        
    def print_person(self):
        print("Your personal data is: ")
        print("First name is:", self.fname)
        print("Last name is:", self.lname)
        print("Nationality is:", self.naionality)
        
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
        
person = Person(fname, lname, age, nationality)
person.print_person()

class Student(Person):
    def __init__(self, fname, lname, age, nationality, university, yearsofstudy):
        super().__init__(fname, lname, age, nationality)
        
        self.university = university
        self.yearofstudy = yearsofstudy
        
    def print_person(self):
        print("Your personal data is: ")
        print(f"First name: {self.fname}")
        print(f"Last name: {self.lname}")
        print(f"Nationality: {self.naionality}")
        print(f"University: {self.university}")
        print(f"Years of study: {self.yearofstudy}")
        
    def welcome_person(self):
        print("Welcome", self.fname, self.lname, "in", self.university, "during", self.yearofstudy)

university = input("Enter university: ")
yearofstudy = int(input("Enter your first year: "))
        
person = Student(fname, lname, age, nationality, university, yearofstudy)
person.print_person()
person.welcome_person()

class Lecturer(Person):
    def __init__(self, fname, lname, age, nationality, university, experience):
        super().__init__(fname, lname, age, nationality)
        
        self.university = university
        self.experience = experience
        
    def print_lecturer(self):
        print("Your personal data is: ")
        print(f"First name: {self.fname}")
        print(f"Last name: {self.lname}")
        print(f"University: {self.university}")
        print(f"Experience: {self.experience}")
        
university = input("Enter university: ")
experience = input("Enter your experience: ")

lecturer = Lecturer(fname, lname, age, nationality, university, experience)
lecturer.print_lecturer()

class Salary(Lecturer):
    def __init__(self, fname, lname, age, nationality, university, experience, payment, hours):
        super().__init__(fname, lname, age, nationality, university, experience)
        
        self.payment = payment 
        self.hours = hours
        
    def salary(self):
       result = (self.payment * self.hours * self.experience)  
       print("Your salry is:", result)  
    
    
payment = int(input("Enter payment: "))
hours = int(input("Enter working hours: "))

salary = Salary(fname, lname, age, nationality, university, experience, payment, hours)
salary.salary()