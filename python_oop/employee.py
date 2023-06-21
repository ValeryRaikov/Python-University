class Employee:
    
    raise_money = 1.05
    number_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@.com"
        self.pay = pay
        
    number_of_emps += 1
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def print_emp_info(self):
        return f"Employee --> {self.fullname()},\nEmail --> {self.email},\nPayment --> {self.pay}"
    
    def raise_amt(self):
        self.raise_moneyraise_money = 1.10
        self.pay = int(self.raise_money * self.pay)
        return f"{self.fullname()}'s new salary is {self.pay}"
    

emp_1 = Employee("Valery", "Raykov", 60000)
emp_2 = Employee("Ivan", "Motovski", 50000)

print(emp_1.fullname())
print(emp_1.print_emp_info())
print(emp_1.raise_amt())

emp_2.raise_money =  1.05
print(emp_2.raise_amt())

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang, experience):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.experience = experience
        
    def print_developer(self):
        if self.experience > 10:
            return f"Developer --> {self.fullname()} is a team lead with {self.prog_lang}."
        elif self.experience > 5:
            return f"Developer --> {self.fullname()} is a senior developer with {self.prog_lang}."
        else:
            return f"Developer --> {self.fullname()} is a junior developer with {self.prog_lang}."
        
dev_1 = Developer("Peter", "Stamatov", 80000, "Python", 6)
dev_2 = Developer("Maria", "Angelova", 75000, "C#", 4)

print(dev_1.print_developer())
print(dev_2.print_developer())

class Manager(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)
        self.emps = []
        
    def manager_task(self):
        for emp in Employee.print_emp_info(self):
            self.emps.append(self.fullname())
        return f"Manager --> {self.fullname()} is responsible for {self.emps} employees."
    
man_1 = Manager("Danail", "Petrov", 120000)   

print(man_1.manager_task())