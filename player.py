import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from card import window
from card import Images
from deck import Deck


class Player(object):
    def __init__(self, is_player_one, point_total, point_multiplier=1, ddong_count=0, go_count=0, gwang_count=0, pi_count=0, gguet_count=0, win=False, first_turn_ddong=False, required_point_total_to_win=7):
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
        self.first_turn_ddong = first_turn_ddong
        self.required_point_total_to_win = required_point_total_to_win

    def lay_down_random_card(self, cards_in_hand, shuffled_deck, current_player, waiting_player):
        length = len(cards_in_hand) - 1
        card_index = random.randint(0, length)
        lay_down = self.cards_in_hand.pop(card_index)

        if lay_down.month == 14:
            while lay_down.month == 14:
                current_player.cards_on_board.append(lay_down)
                replacement_card = current_player.draw_card(shuffled_deck)
                current_player.cards_in_hand.append(replacement_card)
                lay_down = current_player.lay_down_random_card(current_player.cards_in_hand, shuffled_deck, current_player,waiting_player)
                self.steal_pi(current_player, waiting_player)
                #print("played a bonus card - stole a pi using bonus card")

        return lay_down

    def steal_pi(self, stealing_player, giving_player):
        pi_exists = False
        for i in giving_player.cards_on_board:
            if i.category == 4 and not pi_exists:
                #print("We stole a PI!")
                pi_exists = True
                stealing_player.cards_on_board.append(i)
                giving_player.cards_on_board.remove(i)
        if not pi_exists:
            for i in giving_player.cards_on_board:
                if i.category == 5 or i.category == 7 or i.category == 8:
                    #print("We stole a Two_PI!")
                    pi_exists = True
                    stealing_player.cards_on_board.append(i)
                    giving_player.cards_on_board.remove(i)

    def lay_down_chosen_card(self, cards_in_hand, the_card, card_list, card_button):
        lay_down = self.cards_in_hand.remove(the_card)
        card_button.destroy()
        #lay_down = the_card
        #print("We laid down: ", lay_down.name, lay_down.month, lay_down.category)
        #print("We laid down: ", the_card.name, the_card.month, the_card.category)
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
