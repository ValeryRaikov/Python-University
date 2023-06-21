class FishingRod:
    def __init__(self, brand, model, type, year, price, rating):
        self.brand = brand
        self.model = model
        self.type = type
        self.year = year
        self.price = price
        self.rating = rating
        
    def __str__(self):
        return f"Fishing rod: {self.brand} {self.model}, {self.type}, {self.year}, {self.price}$, {self.rating}/10 stars"
    
    def __repr__(self):
        return f"Fishing rod: {self.brand} {self.model}, {self.type}, {self.year}, {self.price}$, {self.rating}/10 stars"
    
rod1 = FishingRod("Italica", "Redfifty", "bolognese", 2019, 600, 9.1)
rod2 = FishingRod("Formax", "Visage bolo", "bolognese", 2021, 180, 7.4)
rod3 = FishingRod("SavageGear", "Xlnt3", "spinning", 2020, 160, 7.8)
rod4 = FishingRod("Filstar", "Tortuga tele-bomb", "t-match", 2020, 100, 8.1)

rods = [rod1, rod2, rod3, rod4]

def print_rods():
    for rod in rods:
        print(rod)

print_rods()

def sort_by_price():
    print(sorted(rods, key=lambda x: x.price, reverse = True))
    
sort_by_price()

def check_rod(brand):
    isPresent = False
    for rod in rods:
        if rod.brand == brand:
            isPresent = True
            print(rod)
    if not isPresent:
        print("No such rod!")
        
check_rod(brand = input("Check for rod: "))

def add_rod():
    new_brand = input("Enter brand: ")
    new_model = input("Enter model: ")
    new_type = input("Input type: ") 
    new_year = int(input("Enter year: "))
    new_price = float(input("Enter price: "))
    new_rating = float(input("Enter rating: "))
    
    new_rod = FishingRod(new_brand, new_model, new_type, new_year, new_price, new_rating)
    rods.append(new_rod)
    
add_rod()