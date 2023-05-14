import random

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        ranks = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        deck = [Card(rank, suit) for rank in ranks for suit in suits]
        return deck

    def shuffle(self):
        random.shuffle(self.cards)
