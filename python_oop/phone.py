class Phone:
    def __init__(self, phone_brand, phone_model, phone_year, phone_color, phone_price, new_list):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.phone_year = phone_year
        self.phone_color = phone_color
        self.phone_price = phone_price
        
    def sort_price(self):
        self.new_list = sorted(this_list, key = lambda x : x[4])
    
    def sort_phones(self):
        self.new_list = sorted(this_list, key = lambda x : x[0])
    
    def save_changes(self):
        with open("results.txt", "w") as f:
            f.write()
    
phone1 = Phone("Samsung", "Galaxy S 22", "2022", "black", 1900)
phone2 = Phone("Iphone", "12 Pro", "2021", "white", 2500)
phone3 = Phone("Huawei", "Nova 9", "2020", "grey", 999)

this_list = [phone1, phone2, phone3]