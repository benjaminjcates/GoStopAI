from deck import Deck


class Player(object):
    def __init__(self, is_player_one, deck):
        self.cards_in_hand = []
        self.cards_on_board = []
        self.is_player_one = is_player_one
        self.deck = deck

    def draw_card(self, the_deck):
        drawn_card = the_deck.pop(0)
        return drawn_card

    def lay_down_card(self, is_player_one, current_hand):
        print("nothing")

    #def hand_of_cards(self, is_player_one, deck):


class HandOfCards(Player):
    def get_hand_of_cards(self):
        return self.cards_in_hand

    def set_hand_of_cards(self, cards):
        self.cards_in_hand = cards

    #def hand_details(self):
    #    for i in range(len(self.cards)):
    #        print(i.name, i.month, i.category)
            

#class TableCards(CardList):
#    def get_paired_cards(self, card):
#        paired_cards = []
#        for match_card in self.cards:
#            if match_card.month == card.month:
#                paired_cards.append(match_card)
#
#        return paired_cards
