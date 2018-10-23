from deck import deck

class dealer:

    hand = []
    hand_value = 0

    def __init__(self,name):
        self.name = name
    
    def hit(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def addCards(self,*cards):
        for c in cards:
            self.hand.append(c)

    def handValue(self):
        self.hand_value = sum([c.getValue() for c in self.hand])        
        return self.hand_value

    def showCard(self):
        if self.hand:
            print('Dealer shows {0} ({1})'.format(self.hand[0].getValue(),self.hand[0].getType()))
        else:
            print("error: Dealer has no cards to show!")

    def showBothCards(self):
        if self.hand:
            print('Dealer shows {0} ({1} {2})'.format(self.handValue(),self.hand[0].getType(),self.hand[1].getType()))       
    
    def isBust(self):
        if self.handValue() > 21:
            return True
        
    def emptyHand(self):
        self.hand_value = 0
        self.hand = []    