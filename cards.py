import random
drawn_cards = list()

def DecodeName(input_str):
    if input_str == "NA":
        return "No more cards"
    raw_str = input_str.split(':')
    suit = int(raw_str[0])
    card = int(raw_str[1])
    card_str = ""
    if (card > 1 and card < 11):
        card_str = str(card)
    else:
        card_str = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }.get(card, "Unknown")
    suit_str = {
        0: "Clubs",
        1: "Diamonds",
        2: "Hearts",
        3: "Spades"
    }.get(suit, "Unknown")
    return card_str + " of " + suit_str
def DrawCard():
    global drawn_cards
    if len(drawn_cards) >= 52:
        print(DecodeName("NA"))
    else:
        found_card = False
        while not found_card:
            suit = str(random.randint(0, 3))
            card = str(random.randint(1, 13))
            formatted_card = suit + ":" + card
            if formatted_card not in drawn_cards:
                found_card = True
                drawn_cards.append(formatted_card)
                print(DecodeName(formatted_card))

for k in range (0, 53):
    DrawCard()
