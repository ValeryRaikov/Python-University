med_list = []

class Medicine:
    def __init__(self, name, code, price, quantity, brand):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        self.brand = brand
        
    def __repr__(self):
        return f"{self.name} {self.code} {self.price} {self.quantity} {self.brand}"
        
    def display(self):
        print(f"{self.name} {self.code} {self.price} {self.quantity} {self.brand}")
        
    def search_by_name(self, name):
        isFound = False
        for med in med_list:
            if med.name == name:
                isFound = True
                print(med)
        if not isFound:
            print("Med not found!")
  
med_1 = Medicine("A", 123, 10, 2, "ABC")
med_2 = Medicine("B", 125, 15, 4, "ACC")
med_list = [med_1, med_2]
                
Medicine.search_by_name(med_list, "A")
med_1.display()