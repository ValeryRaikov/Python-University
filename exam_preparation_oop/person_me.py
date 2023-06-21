class Person:
    def __init__(self, name, age, hometown, email):
        self.name = name
        self.age = age
        self.hometown = hometown
        self.email = email
        
    def __repr__(self):
        return f"{self.name} | {self.age} | {self.hometown} | {self.email}"
    
people = [
    Person("Valery", 19, "Sofia", "valery@gmail.com"), 
    Person("Hristina", 19, "Sofia", "hrisi@gmail.com"),
    Person("Ivan", 17, "Burgas", "ivan@abv.bg"),
]

def sort_by_age(people):
    print(sorted(people, key = lambda x: x.age))
    
sort_by_age(people)

people_info = []
for person in people:
    person = {
        "Name": person.name, 
        "Age": person.age, 
        "Hometown": person.hometown, 
        "Email": person.email
    }
    people_info.append(person)
    
print(people_info)

def check_dict(people_info, name):
    for person in people_info:
        if person["Name"] == name:
            person["Name"] = input("Set a new name: ")
            
    print(people_info)
            
check_dict(people_info, "Hristina")