import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from card import window
from card import Images
from deck import Deck


class Player(object):
    def __init__(self, is_player_one, point_total, point_multiplier=1, ddong_count=0, go_count=0, gwang_count=0, pi_count=0, gguet_count=0, win=False):
        self.cards_in_hand = []
        self.cards_on_board = []
        self.is_player_one = is_player_one
        self.point_total = point_total
        self.point_multiplier = point_multiplier
        self.ddong_month = []
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

    def lay_down_chosen_card(self, cards_in_hand, the_card, card_list, card_button):
        lay_down = self.cards_in_hand.remove(the_card)
        card_button.destroy()
        #lay_down = the_card
        #print("We laid down: ", lay_down.name, lay_down.month, lay_down.category)
        print("We laid down: ", the_card.name, the_card.month, the_card.category)
        #return lay_down
        if len(cards_in_hand) == 0:
            print("No cards left")

        """
        player_one_card_list = []
        player_two_card_list = []
        communal_cards_list = []
        player_one_board_list = []
        player_two_board_list = []

        count = 0
        #card_button_player_one = ttk.Button(master=window, image=i.image, command=lambda the_card=the_card: self.player_one.lay_down_chosen_card(self.player_one.cards_in_hand, the_card, player_one_card_list, card_button_player_one))
        card_button_player_one = ttk.Label(master=window, image=the_card.image)
        #card_button_player_one['command'] = lambda the_card=the_card, button_inst = card_button_player_one: self.player_one.lay_down_chosen_card(self.player_one.cards_in_hand, the_card, player_one_card_list, button_inst)
        player_one_card_list.append(card_button_player_one)
        player_one_card_list[3].grid(row=3, column=count, sticky="nsew")

        """

    def test_two(self):
        print("I'm Ben")

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
