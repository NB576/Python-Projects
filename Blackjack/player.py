
class player:

    hand = []
    hand_value = 0

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def place_bet(self):
        while True:    
            try:    
                bet = int(input("Bet amount: "))
                if bet <= self.balance:
                    print("Bet of {} placed".format(bet))
                    self.balance -= bet 
                    break
                else:
                    print("Unavailable funds")
            except:
                print("Invalid input. Please try again")
        return bet

    def showBothCards(self):
        if self.hand:
            print('{0} has {1} ({2} {3})'.format(self.name,self.handValue(),self.hand[0].getType(),self.hand[1].getType()))       
    
    def addCards(self,*cards):
        for c in cards:
            self.hand.append(c)

    def handValue(self):
        self.hand_value = sum([c.getValue() for c in self.hand])
        return self.hand_value

    def addBalance(self,amount):
        self.balance += amount

    def isBust(self):
        return self.handValue() > 21

    def emptyHand(self):
        self.hand_value = 0
        self.hand = []
    

        



