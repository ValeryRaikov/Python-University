class Coffee:
    
    def __init__(self, temperature):
        self.temperature = temperature
        
    def coffee_cup(self):
        if self.temperature >= 60:
            output_line = "Coffee too hot"
        elif self.temperature <= 30:
            output_line = "Coffee too cold"
        else:
            output_line = "Coffee Ok to drink"
            
        print(output_line)
            
cup = Coffee(temperature = float(input("Enter coffee temperature: ")))
cup.coffee_cup()