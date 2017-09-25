# Blackjack By Brandon Riley
# 9/22/17
# A very simple blackjack game

import random


def draw_card():
    """
    Gets the number of a new card
    :return: Number between 1 and 10
    """
    return random.randint(1, 10)


def over_twenty_one(total):
    """
    Checks if total is over 21
    :param total: Player's total card count
    :return: True or False
    """
    if total > 21:
        print("----------------------------------------------------------------------------------------------")
        print("You went over 21")
        print("YOU LOSE")
        return False
    else:
        return True


def dealers_hand():
    """
    Gets cards and total for the dealer
    :return: Total of dealers cards
    """
    dealers_card_one = draw_card()
    dealers_card_two = draw_card()
    dealers_sum = dealers_card_one + dealers_card_two
    print("----------------------------------------------------------------------------------------------")
    print("The Dealer has a", dealers_card_one, "and a", dealers_card_two)
    print("The Dealer's total is", dealers_sum)
    print("----------------------------------------------------------------------------------------------")
    return dealers_sum


def who_won(total, dealers_sum):
    """
    Checks and prints who won
    :param total: Player's total card count
    :param dealers_sum: Dealer's total card count
    :return:
    """
    if dealers_sum > total:
        print("YOU LOSE")
    if total > dealers_sum:
        print("YOU WIN")
    if dealers_sum == total:
        print("YOU LOSE")


def main():
    card_one = draw_card()
    card_two = draw_card()
    total = card_one + card_two
    print("You drew a", card_one, "and a", card_two)
    print("Your total is", total)
    new_card = input("Would you like to draw another card?")
    if new_card == "y":
        print("----------------------------------------------------------------------------------------------")
        card_three = draw_card()
        total += card_three
        print("You drew a", card_three, "and your total is now", total)
        if over_twenty_one(total):
            dealers_sum = dealers_hand()
            who_won(total, dealers_sum)
    if new_card == "n":
        dealers_sum = dealers_hand()
        who_won(total, dealers_sum)

main()
