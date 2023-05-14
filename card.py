class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def numeric_value(self):
        if isinstance(self.rank, int):
            return self.rank
        elif self.rank == "Jack":
            return 11
        elif self.rank == "Queen":
            return 12
        elif self.rank == "King":
            return 13
        elif self.rank == "Ace":
            return 14

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.numeric_value() == other.numeric_value()
        return False

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.numeric_value() < other.numeric_value()
        return False

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.numeric_value() > other.numeric_value()
        return False