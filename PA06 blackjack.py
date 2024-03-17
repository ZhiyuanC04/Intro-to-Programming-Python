# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def card_to_value(card):
    """
    This function takes as input a str variable card. This function returns the numeric blackjack score of the card.
    :param card:
    :return: Numeric blackjack score of the card.
    """
    card = str(card)
    card = card.upper()
    if card == "T" or card == "J" or card == "Q" or card == "K":
        return int(10)
    elif card == "A":
        return int(1)
    else:
        return int(card)

def hard_score(hand):
    """
    This function returns the “hard” score of the hand.
    :param hand: Function takes in a hand as a string, where each character is a card.
    :return: "Hard” score of the hand.
    """
    hand = str(hand)
    z = 0
    total = 0
    while z < len(hand):
        calc = card_to_value(hand[z])
        total += calc
        z += 1
    return total

def soft_score(hand):
    """
    In this function, the first ace, and only the first ace, is treated as being worth 11 points.
    :param hand: Function takes in a hand as a string, where each character is a card.
    :return: "Soft” score of the hand.
    """
    hand = str(hand)
    y = 0
    z = 0
    total = 0
    while z < len(hand):
        if y < 1 and hand[z] == "A":
            total += 11
            y += 1
            z += 1
        else:
            calc = card_to_value(hand[z])
            total += calc
            z += 1
    return total
