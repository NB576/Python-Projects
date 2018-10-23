from card import card
import random

class deck:

    deck = [card('2h',2),card('3h',3),card('4h',4),card('5h',5),card('6h',2),
            card('7h',7),card('8h',8),card('9h',9),card('10h',10),card('Jh',10),
            card('Qh',10),card('Kh',10),card('Ah',11),card('2d',2),card('3d',3),
            card('4d',4),card('5d',5),card('6d',2),card('7d',7),card('8d',8),
            card('9d',9),card('10d',10),card('Jd',10),card('Qd',10),card('Kd',10),
            card('Ad',11),card('2c',2),card('3c',3),card('4c',4),card('5c',5),
            card('6c',6),card('7c',7),card('8c',8),card('9c',9),card('10c',10),
            card('Jc',10),card('Qc',10),card('Kc',10),card('Ac',11),card('2s',2),
            card('3s',3),card('4s',4),card('5s',5),card('6s',2),card('7s',7),
            card('8s',8),card('9s',9),card('10s',10),card('Js',10),card('Qs',10),
            card('Ks',10),card('As',11)]
                        
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.deck *= num_decks

    def shuffle(self):
        random.shuffle(self.deck)

    def initial_hand(self,person):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def draw_card(self, person):
        card = random.choice(self.deck)
        self.deck.remove(card)
        print("{0} draws {1} ".format(person,card.getType()))
        return card

    def reset(self):
        self.deck = [card('2h',2),card('3h',3),card('4h',4),card('5h',5),card('6h',6),
                card('7h',7),card('8h',8),card('9h',9),card('10h',10),card('Jh',10),
                card('Qh',10),card('Kh',10),card('Ah',11),card('2d',2),card('3d',3),
                card('4d',4),card('5d',5),card('6d',6),card('7d',7),card('8d',8),
                card('9d',9),card('10d',10),card('Jd',10),card('Qd',10),card('Kd',10),
                card('Ad',11),card('2c',2),card('3c',3),card('4c',4),card('5c',5),
                card('6c',6),card('7c',7),card('8c',8),card('9c',9),card('10c',10),
                card('Jc',10),card('Qc',10),card('Kc',10),card('Ac',11),card('2s',2),
                card('3s',3),card('4s',4),card('5s',5),card('6s',6),card('7s',7),
                card('8s',8),card('9s',9),card('10s',10),card('Js',10),card('Qs',10),
                card('Ks',10),card('As',11)]



    


    


