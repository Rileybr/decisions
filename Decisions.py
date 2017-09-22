import random


def draw_card():
    return random.randint(1, 10)


def over_twenty_one(total):
    if total > 21:
        print("----------------------------------------------------------------------------------------------")
        print("You went over 21")
        print("YOU LOSE")
        return False
    else:
        return True


def dealers_hand():
    dealers_card_one = draw_card()
    dealers_card_two = draw_card()
    dealers_sum = dealers_card_one + dealers_card_two
    print("----------------------------------------------------------------------------------------------")
    print("The Dealer has a", dealers_card_one, "and a", dealers_card_two)
    print("The Dealer's total is", dealers_sum)
    print("----------------------------------------------------------------------------------------------")
    return dealers_sum


def who_won(total, dealers_sum):
    if dealers_sum > total:
        print("YOU LOSE")
    if total > dealers_sum:
        print("YOU WIN")


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
        total = card_three + card_two + card_one
        print("You drew a", card_three, "and your total is now", total)
        if over_twenty_one(total):
            dealers_sum = dealers_hand()
            who_won(total, dealers_sum)
    if new_card == "n":
        dealers_sum = dealers_hand()
        who_won(total, dealers_sum)

main()
