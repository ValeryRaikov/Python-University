class Employee:
    
    raise_pay = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first +  "." + self.last + "@company.gmail.com"
        
    def raise_payment(self):
        emp_1.raise_pay = 1.1
        self.pay = int(self.pay * self.raise_pay)
        
    def print_info(self):
        print(self.first, self.last, "earns", self.pay)
        print("Contact:", self.email)
    
emp_1 = Employee("Valery", "Raykov", 45000)
emp_2 = Employee("Ivan", "Motovski", 40000)
emp_3 = Employee("Martin", "Velchev", 30000)

emp_1.print_info()
print()
emp_2.print_info()
print()
emp_3.print_info()

print(emp_1.first, emp_1.last, "raise in salary is:", emp_1.raise_pay)
print(emp_2.first, emp_2.last, "raise in salary is:", emp_2.raise_pay)
print(emp_3.first, emp_3.last, "raise in salary is:", emp_3.raise_pay)

emp_1.raise_payment()
emp_2.raise_payment()
emp_3.raise_payment()

print("New salary is:", emp_1.pay)
print("New salary is:", emp_2.pay)
print("New salary is:", emp_3.pay)