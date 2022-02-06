import random

import card
from card import Card
from card import ALL_CARDS

class Deck:

    def __init__(self):
        self.cards = ALL_CARDS

    def create_deck(self, all_cards):
        new_deck = list(all_cards)
        return new_deck

    def shuffle(self, my_list):
        random.shuffle(my_list)
        shuffled_list = my_list
        return shuffled_list

    #def draw_card(self, the_deck):
    #    drawn_card = the_deck.pop(0)
    #    return drawn_card

    def deck_size(self, my_list):
        length = len(my_list)
        return length
