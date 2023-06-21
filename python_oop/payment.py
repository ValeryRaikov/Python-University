class MonthlyPayment:
    def __init__(self, name, family, worked_years, job_title):
        self.name = name
        self.family = family
        self.worked_years = worked_years
        self.job_title = job_title
        
    def print(self):
        print(self.name, self.family, self.worked_years, self.job_title)
        
    def payment(self):
        return self.worked_years * 10
        
monthly_payment = MonthlyPayment("Valery", "Raykov", 19, "student")
monthly_payment.print()     
    
print(monthly_payment)