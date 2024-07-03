# ============================================================================#
# Programmer : Walter Reeves
# Art Creator: Dr. Angela Yu
#
# Description:
#    This program plays a simple game of blackjack.
#
# Further Improvement:
#    Add a total score tracker.
#    Display the total score after all rounds are finished.
#    Add an exit condition if player/dealer has card value of 21 initially.
# ============================================================================#
import os
import random

from art import logo

# Global dictionaries.
card_values = {
    "A": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "1": 10,  # "1" = Ten
    "J": 10,
    "Q": 10,
    "K": 10
}

# Global lists.
all_cards = [
    "A♠",
    "2♠",
    "3♠",
    "4♠",
    "5♠",
    "6♠",
    "7♠",
    "8♠",
    "9♠",
    "10♠",
    "J♠",
    "Q♠",
    "K♠",
    "A♣",
    "2♣",
    "3♣",
    "4♣",
    "5♣",
    "6♣",
    "7♣",
    "8♣",
    "9♣",
    "10♣",
    "J♣",
    "Q♣",
    "K♣",
    "A♥",
    "2♥",
    "3♥",
    "4♥",
    "5♥",
    "6♥",
    "7♥",
    "8♥",
    "9♥",
    "10♥",
    "J♥",
    "Q♥",
    "K♥",
    "A♦",
    "2♦",
    "3♦",
    "4♦",
    "5♦",
    "6♦",
    "7♦",
    "8♦",
    "9♦",
    "10♦",
    "J♦",
    "Q♦",
    "K♦",
]


# ============================================================================#
#  Plays a game of blackjack.
# ============================================================================#
def game():
    # Local lists.
    dealer_cards = []
    player_cards = []

    # Local variables.
    card_sum_player = 0
    player_card_counter = 2
    round_number = 1
    dealer_text = "the Dealer's"
    player_text = "your"

    # ==========================================================================#
    #  Gets the first two player cards.
    # ==========================================================================#
    def initial_player_cards():

        player_card_one_position = random.randint(0, len(all_cards) - 1)
        player_cards.append(all_cards[player_card_one_position])
        all_cards.pop(player_card_one_position)
        player_card_two_position = random.randint(0, len(all_cards) - 1)
        player_cards.append(all_cards[player_card_two_position])
        all_cards.pop(player_card_two_position)

    # ==========================================================================#
    #  Displays the current held cards.
    # ==========================================================================#
    def print_cards(person_cards, person_text, rounded_num):
        # Modifies the sentence to be grammatically correct.
        if person_text == player_text:
            print(f"{person_text.title()} cards", end=": ")
        elif person_text == dealer_text and rounded_num != -1:
            print(f"{person_text} shown card is", end=": ")
        else:
            print(f"{person_text} cards were", end=": ")

        # Displays all cards unless cards belong to dealer, and it's not endgame.
        if rounded_num != -1 and person_cards == dealer_cards:
            print(person_cards[0])
        else:
            for xCard in range(len(person_cards)):
                # Displays final card without comma
                if xCard == len(person_cards) - 1:
                    print(person_cards[xCard])
                # Displays cards with comma separator
                else:
                    print(person_cards[xCard], end=", ")

    # ==========================================================================#
    #  Gets the numerical ace value.
    # ==========================================================================#
    def get_ace_value():
        ace_val = -1

        while ace_val == -1:
            ace_val = int(input("Would you like your ace to be 1 or 11? "))
            if ace_val == 1:
                ace_val = 0
            elif ace_val == 11:
                ace_val = 1
            else:
                print("Invalid Input.")
                ace_val = -1

        return ace_val

    # ==========================================================================#
    #  Calculates the total sum of the cards
    # ==========================================================================#
    def sum_cards(person_cards):
        card_value_sum = 0

        for xCard in range(len(person_cards)):
            # Sums specific ace values for player.
            if person_cards == player_cards and person_cards[xCard][0] == "A":
                ace_val = get_ace_value()
                card_value_sum += int(card_values["A"][ace_val])

            # Sums specific ace values for dealer.
            elif person_cards == dealer_cards and person_cards[xCard][0] == "A":
                if card_value_sum <= 10 and person_cards == dealer_cards:
                    ace_val = 1
                else:
                    ace_val = 0
                card_value_sum += int(card_values["A"][ace_val])

            # Sums for non-ace values.
            else:
                card_value_sum += int(card_values[person_cards[xCard][0]])

        return card_value_sum

    # ==========================================================================#
    #  Gets the first two dealer cards.
    # ==========================================================================#
    def initial_dealer_cards():
        x_card = 0
        dealer_sum = sum_cards(dealer_cards)

        # Continues to draw dealer cards until the total value is a minimum of 16.
        while dealer_sum <= 16:
            dealer_card_position = random.randint(0, len(all_cards) - 1)
            dealer_cards.append(all_cards[dealer_card_position])
            all_cards.pop(dealer_card_position)
            dealer_sum = sum_cards(dealer_cards)
            x_card += 1

    # ==========================================================================#
    #  Displays the card value sum.
    # ==========================================================================#
    def display_sum(person_card_sum, person_text):
        print(f"The sum of {person_text} cards is: {person_card_sum}")

    # ==========================================================================#
    #  Determines the winner.
    # ==========================================================================#
    def win_condition():
        round_num = -1
        dealer_sum = sum_cards(dealer_cards)

        print("\n====== ROUND SCORE ======")
        print_cards(player_cards, player_text, round_num)
        print(f"{player_text} card final sum is: {card_sum_player}.")
        print_cards(dealer_cards, dealer_text, round_num)
        print(f"{dealer_text} card final sum is: {dealer_sum}.")  # ERROR

        # Player and Dealer went over 21.
        if card_sum_player > 21 and dealer_sum > 21:
            print("Everyone went over 21, everyone loses.")
            winner = "no one"
        # Player went over 21.
        elif card_sum_player > 21:
            print("You went over 21, you lost.")
            winner = dealer_text
        # Dealer went over 21
        elif dealer_sum > 21:
            print("You win, dealer went over 21.")
            winner = player_text
        # Dealer has higher cards under 21
        elif card_sum_player < dealer_sum:
            print("Dealer had higher cards, you lost.")
            winner = dealer_text
        # Player has higher cards under 21
        elif card_sum_player > dealer_sum:
            print("Congratulations, you beat the dealer!")
            winner = player_text
        # Player and Dealer had same card value.
        else:
            print("Everyone had the same card value.")
            winner = "no one"

        return winner

    # Start of Game
    initial_player_cards()
    initial_dealer_cards()

    # Shows player their cards, current score, and dealer's first card
    print_cards(player_cards, player_text, round_number)
    card_sum_player = sum_cards(player_cards)
    display_sum(card_sum_player, player_text)
    print_cards(dealer_cards, dealer_text, round_number)

    # Prompts player to draw a new card.
    draw_new_card = input("Would you like to draw another card (y/n)? ")
    draw_new_card = draw_new_card.lower()

    while draw_new_card == "y" and card_sum_player < 21:
        player_card_counter += 1

        # Adds new card to current cards
        new_card_position = random.randint(0, len(all_cards) - 1)
        player_cards.append(all_cards[new_card_position])
        all_cards.pop(new_card_position)

        # Asks user for ace value if the new card is an ace.
        if player_cards[player_card_counter - 1][0] == "A":
            ace_value = get_ace_value()
            card_sum_player += card_values["A"][ace_value]
        else:
            card_sum_player += int(card_values[player_cards[player_card_counter - 1][0]])

        # Displays cards after new card is chosen
        print_cards(player_cards, player_text, round_number)
        display_sum(card_sum_player, player_text)

        if card_sum_player < 21:
            draw_new_card = input("Would you like to draw another card (y/n)? ")
            draw_new_card = draw_new_card.lower()

    win_condition()
    input("\nPress any key to continue.")


# ============================================================================#
#  Start of main.
# ============================================================================#
play_game = input("Would you like to play Blackjack (y/n)? ")
play_game = play_game.lower()

while play_game != 'n':
    if play_game == 'y':
        print(logo)
        game()
        os.system("clear")

    else:
        print("Invalid Input.")
    play_game = input("Would you like to play Blackjack (y/n)? ")
    play_game = play_game.lower()

else:
    print("Thank you for visiting!")
