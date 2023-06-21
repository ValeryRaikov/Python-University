class Person:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        
    def print_person(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.nationality)
        
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
        
person = Person(first_name, last_name, age, nationality)
person.print_person()

class Student(Person):
    def __init__(self, first_name, last_name, age, nationality, university, yearsofstudy):
        super().__init__(first_name, last_name, age, nationality)
        
        self.university = university
        self.yearofstudy = yearsofstudy   
        
    def print_people(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Nationality: {self.nationality}")
        print(f"University: {self.university}")
        print(f"Years of study: {self.yearsofstudy}")