import random
class Card:
    def __init__(self,rank="",suit=""):
        self.rank=rank
        self.suit=suit
    def selectRandom(self):
        ranks=["ace","2","3","4","5","6","7","8","9","jack","quin","king"]
        suits=["spades","hearts","diamonds","clubs"]
        self.rank=random.choice(ranks)
        self.suit=random.choice(suits)
    def __str__(self):
        return(self.rank+ " of " +self.suit)
        
def main():
    c=Card()
    c.selectRandom()
    print(c)
    
main()
