class Medicine:
    def __init__(self, name, code, price, quantity, brand):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        self.brand = brand
        
    def __repr__(self):
        return f"{self.name} {self.code} {self.price} {self.quantity} {self.brand}"
        
    def find_by_name(med_list, name):
        isFound = False
        for med in med_list:
            if med.name == name:
                isFound = True
                print(med)
        if not isFound:      
            print("Medicine not found!")
            
    def sold_meds(med_list, sold, loaded):
        for med in med_list:
            med.quantity -= sold
            print(med.quantity)
            med.quantity += loaded
            print(med.quantity)
                
med_list = [
    Medicine("A", 1001, 15, 3, "ABC"), 
    Medicine("B", 1002, 12, 2, "ABD"), 
    Medicine("A", 1005, 25, 1, "ABF"), 
    Medicine("G", 1007, 10, 5, "ACC")
]

Medicine.find_by_name(med_list, "A")
Medicine.sold_meds(med_list, 2, 4)