class Cart:
    def __init__(self, manifacturer, code, price, quantity):
        self.manifacturer = manifacturer
        self. code = code
        self. price = price
        self.quantity = quantity
        
    def __repr__(self):
        return f"Purchase --> {self.manifacturer}, {self.code}, {self.price}, {self.quantity}"
 
router_models = ["Xiaomi Mi Router 4C", "Xiaomi Mi Router 4A", "TP-Link Archer C54 AC1200", "TP-Link Archer C80 AC1900"]
    
routers_all = []

for router in router_models:
    router_info = router.split(" ")
    
    manifacturer = router_info[0]
    code = router_info[-1]
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    current_router = Cart(manifacturer, code, price, quantity)
    routers_all.append(current_router)
    
def add_router():
    new_manifacturer = input("Enter manifacturer: ")
    new_code = input("Enter code: ")
    new_price = float(input("Enter price: "))
    new_quantity = int(input("Enter quantity: "))
    
    new_router = Cart(new_manifacturer, new_code, new_price, new_quantity)
    routers_all.append(new_router)
    
    print(routers_all)
    
dds = float(input("Enter DDS: "))
price_delivery = float(input("Enter price: "))

def end_price(routers_all, dds, price_delivery):
    with open("price.txt", "w") as wf:
        for current_router in routers_all:
            price_dds = (current_router.price * current_router.quantity) * dds
            total_price = (current_router.price * current_router.quantity) + price_dds + price_delivery
            
            wf.write(f"{current_router.manifacturer} total price of {total_price}\n")
            
end_price(routers_all, dds, price_delivery)
    
add_router()