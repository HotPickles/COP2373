#grabs the random module i need
import random

#the deck object as requested form the book
class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    #keeps track of how many cards are in the deck with counters, shuffles when it runs out, and deals the cards
    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
        self.current_card += 1
        return self.card_list[self.current_card - 1]

#deals the hand of cards straight into a list and returns the result, looking to the deal function to fulfill this
def deal_hand(deck):
    hand = []
    for i in range(5):
        hand.append(deck.deal())
    return hand

#plays sum poker
def poker():
    current_deck = Deck(52)

    #deals the poker hand
    hand = deal_hand(current_deck)
    print("Your hand", hand)

    #asks user which drawn cards they wanna replace.
    replace = input("Enter numbers (1-5) to replace. Use commas ")

    if replace.strip():
        #handles the determination of what the user wants to replace from the input they gave; translates the string into interger(s) and throws them into a list
        intergers_replaced = [int(x) - 1 for x in replace.split(',')]

        # Replace the selected cards
        for i in intergers_replaced:
            hand[i] = current_deck.deal()

    print("New Hand", hand)

#plays the poker
poker()