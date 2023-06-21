import random 


paints = ["Spades", "Hearts","Diamonds", "Clubs"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

class Cards:
    def __init__(self, paint_type, value_type):
        self.paint_type = paint_type
        self.value_type = value_type
        
    def paint(self):
        return self.paint_type
    
    def value(self):
        return self.value_type
    
    def compare_cards_paint(self):
        pass
    
    
card1 = Cards(random.choice(paints), random.choice(values))
print("Paint type for card 1 is:", card1.paint())
print("Value type for card 1 is:", card1.value())
card2 = Cards(random.choice(paints), random.choice(values))
print("Paint type for card 2 is:", card2.paint())
print("Value type for card 2 is:", card2.value())
card3 = Cards(random.choice(paints), random.choice(values))
print("Paint type for card 3 is:", card3.paint())
print("Value type for card 3 is:", card3.value())