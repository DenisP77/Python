
# main.py
# Import the Deck class from my_package
from game_package.deck import Deck
from game_package.player import Player


##################   Simple War Game ######################
# Two players will each start off with half the deck, then they each remove a card,
# compare which card has the highest value, and the player with the higher card wins both cards.


# outside variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


if __name__ == '__main__':

    player_one = Player("One")
    print(player_one)

    player_two = Player("Two")
    print(player_two)

# Setup New Game: Create a new deck with the parameters
    deck = Deck(suits, ranks, values)

# Shuffle the deck
    deck.shuffle()

# Deal one card
#     card = deck.deal_one()
#     print(card)  # Output example: Ace of Spades

# Split the Deck between players
    half_deck = int(len(deck.all_cards)/2) # half_deck = 26 cards
    print(f'half_deck = {half_deck}')

    for x in range(int(half_deck)):
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())

    print(player_one)
    print(player_two)

    # len(deck.all_cards)
    # len(player_one.all_cards)
    # len(player_two.all_cards)
    game_on = True
    round_num = 0

    while game_on:

        round_num += 1
        print(f"Round {round_num}")

        # Check to see if a player is out of cards:
        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break

        # Otherwise, the game is still on!

        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                # Player One gets the cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            # Player Two Has higher Card
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # Player Two gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            else:
                print('WAR!')
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.

                # First check to see if player has enough cards

                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins! Player One Loses!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins! Player One Loses!")
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

