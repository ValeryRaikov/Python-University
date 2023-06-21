import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
        
    def find_peremeter(self):
        find_peremeter = self.a + self.b + self.c
        return find_peremeter
    
    def find_surface(self):
        find_surface = (self.a + self.b + self.c) / 2 * math.sqrt(((self.a + self.b + self.c) / 2 - self.a) * ((self.a + self.b + self.c) / 2 - self.b) * ((self.a + self.b + self.c) / 2 - self.c)) 
        return find_surface
        
peremeter = Triangle(3, 4, 5)        
surface = Triangle(3, 4, 5)  

result1 = peremeter.find_peremeter() 
result2 = surface.find_surface() 

print("The peremeter is:", result1) 
print("The surface is:", round(result2, 2))  