class Medicine:
    def __init__(self, name, code, price, quantity, brand):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        self.brand = brand
        
    def __str__(self):
        return f"{self.name} {self.code} {self.price} {self.quantity} {self.brand}"
    
    def __repr__(self):
        return f"{self.name} {self.code} {self.price} {self.quantity} {self.brand}"
    
medicine = [
    Medicine("A", 1001, 15, 3, "ABC"), 
    Medicine("B", 1002, 12, 2, "ABD"), 
    Medicine("A", 1005, 25, 1, "ABF"), 
    Medicine("G", 1007, 10, 5, "ACC")
]

def find_medicine(name):
    isFound = False
    for med in medicine:
        if med.name ==name:
            isFound = True
            print(med)
            
    if not isFound:
        print("Medicine not found!")
        
def sort_name():
    print(sorted(medicine, key = lambda x: x.name))
    
def find_min_quantity():
    quantities = []
    for med in medicine:
        quantities.append(med.quantity)
    print(f"Min quantity is: {min(quantities)}")
    
find_medicine("A")
sort_name()
find_min_quantity()