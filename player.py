import random

from deck import Deck


class Player(object):
    def __init__(self, is_player_one, deck, point_total, point_multiplier=1, ddong_count=0, go_count=0, gwang_count=0, pi_count=0, gguet_count=0, win=False):
        self.cards_in_hand = []
        self.cards_on_board = []
        self.is_player_one = is_player_one
        self.deck = deck
        self.point_total = point_total
        self.point_multiplier = point_multiplier
        self.ddong_count = ddong_count
        self.go_count = go_count
        self.gwang_count = gwang_count
        self.pi_count = pi_count
        self.gguet_count = gguet_count
        self.win = win


    def lay_down_random_card(self, cards_in_hand):
        length = len(cards_in_hand) - 1
        card_index = random.randint(0, length)
        lay_down = self.cards_in_hand.pop(card_index)
        return lay_down

    #def card_to_play(self, ):

    def draw_card(self, the_deck):
        drawn_card = the_deck.pop(0)
        return drawn_card

    # def hand_of_cards(self, is_player_one, deck):


#class HandOfCards(Player):
#    def get_hand_of_cards(self):
#        return self.cards_in_hand

#    def set_hand_of_cards(self, cards):
#        self.cards_in_hand = cards

    # def hand_details(self):
    #    for i in range(len(self.cards)):
    #        print(i.name, i.month, i.category)
            

# class TableCards(CardList):
#    def get_paired_cards(self, card):
#        paired_cards = []
#        for match_card in self.cards:
#            if match_card.month == card.month:
#                paired_cards.append(match_card)
#
#        return paired_cards
