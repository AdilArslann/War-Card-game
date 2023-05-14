from deck import Deck
from player import Player

def handle_war(player1, player2):
    war_pile = []
    while True:
        player1_cards = [player1.play_card() for _ in range(3)]
        player2_cards = [player2.play_card() for _ in range(3)]

        if not player1_cards or not player2_cards:
            break

        war_pile.extend(player1_cards)
        war_pile.extend(player2_cards)

        top_card1 = player1_cards[-1]
        top_card2 = player2_cards[-1]

        if top_card1 > top_card2:
            player1.hand.extend(war_pile)
            break
        elif top_card1 < top_card2:
            player2.hand.extend(war_pile)
            break
        else:
            continue

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

def display_winner(player1, player2):
    if len(player1.hand) > len(player2.hand):
        print(f"{player1} wins the game!")
    elif len(player1.hand) < len(player2.hand):
        print(f"{player2} wins the game!")
    else:
        print("It's a draw!")

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