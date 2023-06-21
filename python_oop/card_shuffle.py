import random

CARD_SUITES = ["Hearts", "Diamonds", "Clubs", "Spades"]
CARD_VALUES = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

class Cards:
    def __init__(self, suites, values):
        self.suites = suites
        self.values = values
        
class Deck(Cards):
    def __init__(self, suites, values):
        super().__init__(suites, values)
    
    def shuffle_pick(self):
        return f"The random chosen card is: {random.choice(self.values)} of {random.choice(self.suites)}"
    
    
card = Deck(CARD_SUITES, CARD_VALUES)
print(card.shuffle_pick())