class Cars:
    def __init__(self, brand, model, year, fuel_type, fuel_consumption, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.price = price
        
    def print_car(self):
        brand = input("Enter car: ")
        model = input("Enter model: ")
        if brand == self.brand and model == self.model:
            print(f"This is the chosen car:\n{self.brand} {self.model}\nPrice : {self.price}")
        else:
            print("Car not found!")
        
    def more_info(self):
        info = input("Do you want to see full characteristics? ")
        if info in ["Yes", "yes"]:
            print(f"Brand : {self.brand}\nModel : {self.model}\nYear : {self.year}\nFuel_type : {self.fuel_type}\nFuel_consumption : {self.fuel_consumption}/100")
            
    def calculate_fuel(self):
        kilometers = float(input("Enter kilometers: "))
        consumption = kilometers * self.fuel_consumption / 100
        print(f"{self.brand} {self.model} consumption for {kilometers}km = {consumption} liters.")
    
car1 = Cars("BMW", "M2", 2019, "fuel", 16, 149000)
car2 = Cars("Skoda", "Octavia RS", 2017, "diesel", 10, 49000)
"""car3 = Cars("Audi", "Q7", 2021, "diesel", 13, 89500)
car4 = Cars("Volkswagen", "Arteon", 2022, "fuel", 15, 79000)""" 

car1.print_car()
car2.print_car()

car1.more_info()
car2.more_info()

car1.calculate_fuel()
car2.calculate_fuel()