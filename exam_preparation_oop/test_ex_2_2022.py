class GsmMobileDevices:
    def __init__(self, free_space, price, year, manifacturer, mobile_model):
        self. free_space = free_space
        self.price = price
        self.year = year
        self.manifacturer = manifacturer
        self.mobile_model = mobile_model
        
    def __repr__(self):
        return f"Phone --> {self.free_space}, {self.price}, {self.year}, {self.manifacturer}, {self.mobile_model}"
    
phones = [
    GsmMobileDevices(256, 1999, 2022, "Samsung", "S22 Pro"), 
    GsmMobileDevices(128, 1299, 2022, "Huawei", "P20"),
    GsmMobileDevices(512, 2599, 2022, "Samsung", "Z-Flip")
]

def sort_by_space(phones):
    print(sorted(phones, key = lambda x: x.free_space))
    
def manifacturer(phones, manifacturer):
    for phone in phones:
        if phone.manifacturer == manifacturer:
            with open("Phone.json", "w") as wf:
                wf.write(f"{phone}\n")
                
    wf.close()
    
sort_by_space(phones)
manifacturer(phones, manifacturer = input("Enter manifacturer: "))