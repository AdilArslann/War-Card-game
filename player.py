class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return self.name

    def receive_card(self, card):
        self.hand.append(card)

    def play_card(self):
        return self.hand.pop(0)