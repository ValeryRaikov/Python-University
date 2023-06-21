import random

class Dice:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def result(self):
        roll = self.first, self.second
        return roll
        
dice = Dice(random.randint(1, 6), random.randint(1, 6))
print(f"Result is: {dice.result()}")