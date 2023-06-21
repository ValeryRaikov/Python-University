class Vehicle:
    def __init__(self, brand, model, fuel_consumption):
        self.brand = brand
        self.model = model
        self.fuel_consumption = fuel_consumption
        
    def car_type(self):
        print(f"These is the following car:\nBrand : {self.brand}, Model : {self.model}")
        
    def fuel(self):
        print(f"Fuel consumption for {self.brand} {self.model} is:\n{self.fuel_consumption}/100 liters.")
        
    def calculate_fuel(self):
        print("Calculate your own consumption.")
        kilometers = float(input("Enter your kilometers: "))
        consumption = f"{(kilometers * self.fuel_consumption / 100):.2f}"
        print(f"For {kilometers}km, {self.brand} {self.model} will consume {consumption} lites of fuel.")
   
car1 = Vehicle("Skoda", "Octavia", 7.4)    
car2 = Vehicle("Kia", "Stinger", 8.3)
car3 = Vehicle("Audi", "S8", 9.9)

car1.car_type()
car2.car_type()
car3.car_type()

car1.fuel()
car2.fuel()
car3.fuel()

car1.calculate_fuel()
car2.calculate_fuel()
car3.calculate_fuel()

class Sportcar(Vehicle):
    def __init__(self, brand, model, fuel_consumption, max_speed):
        super().__init__(brand, model, fuel_consumption)
        self.max_speed = max_speed
        
    def speed(self):
        print(f"Max speed of sport car {self.brand} {self.model} is {self.max_speed}km/h.")
        
sport_car1 = Sportcar("Ford", "Mustang GT", 12.8, 267)
sport_car2 = Sportcar("Mercedes", "GT 63", 14.2, 314)
sport_car3 = Sportcar("BMW", "E36 M5", 12.5, 258)

sport_car1.speed()
sport_car2.speed()
sport_car3.speed()