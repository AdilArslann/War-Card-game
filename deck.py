import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
        deck = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal(self):
        return self.cards.pop()
