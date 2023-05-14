from deck import Deck
from player import Player

def play_round(player1, player2):
    card1 = player1.play_card()
    card2 = player2.play_card()

    if card1 > card2:
        player1.receive_card(card1)
        player1.receive_card(card2)
    elif card1 < card2:
        player2.receive_card(card1)
        player2.receive_card(card2)
    else:
        print("Tie!")

def play_game():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Deal the cards
    while len(deck.cards) > 0:
        player1.receive_card(deck.deal())
        player2.receive_card(deck.deal())

    # Main game loop
    while len(player1.hand) > 0 and len(player2.hand) > 0:
        play_round(player1, player2)

    display_winner(player1, player2)


if __name__ == "__main__":
    play_game()
