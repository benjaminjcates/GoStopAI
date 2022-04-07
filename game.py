import random

import card
from deck import Deck
from player import Player
from card import Card
from card import ALL_CARDS
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from card import window
from card import Images
import math
import time
#import tensorflow as tf
#print("TensorFlow version:", tf.__version__)



def test():
    print("Hi Jihye")


class Game:
    def __init__(self):
        self.deck = Deck()
        #self.player_one = Player(True, self.deck, 0, 1)
        #self.player_two = Player(False, self.deck, 0, 1)
        self.player_one = Player(True, 0, 1)
        self.player_two = Player(False, 0, 1)
        self.table = Player(False, self.deck, 0, 0)
        self.current_player = self.player_one
        self.current_player_num = 0
        self.waiting_player = self.player_two
        self.waiting_player_num = 0
        self.turn_number = 0
        self.time = 0
        self.bonus_ddong_association_month_one = 0
        self.bonus_ddong_association_month_two = 0
        self.bonus_ddong_card_first_category = 0
        self.bonus_ddong_card_second_category = 0
        self.bonus_card_first = card.BONUS_TEST
        self.bonus_card_second = card.BONUS_TEST
        self.bonus_temp_card = card.BONUS_TEST
        self.bonus_bool = False
        self.game_in_progress = True
        self.replay_game = False


    def setup_game(self, first_to_act):
        # create a new deck
        handsize = 10
        tablesize = 8
        month_array_counter_player_one=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        month_array_counter_player_two=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        month_array_counter_communal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        new_deck = self.deck.create_deck(ALL_CARDS)

        # shuffle the deck
        shuffled_deck = self.deck.shuffle(new_deck)

        # print the shuffled deck in order
        # for c in shuffled_deck:
        # print(c.name, c.month, c.category)

        length = self.deck.deck_size(shuffled_deck)
        # print("The # of remaining cards before pop is " + str(length))
        # drawn_card = self.deck.draw_card(new_deck)


        # set the starting and waiting player
        self.set_starting_player(first_to_act)

        if first_to_act == 1:
            # deal out all the cards
            for i in range(handsize):
                drawn_card = self.player_one.draw_card(shuffled_deck)
                self.player_one.cards_in_hand.append(drawn_card)

            for i in range(handsize):
                drawn_card = self.player_two.draw_card(shuffled_deck)
                self.player_two.cards_in_hand.append(drawn_card)
        else:
            # deal out all the cards
            for i in range(handsize):
                drawn_card = self.player_two.draw_card(shuffled_deck)
                self.player_two.cards_in_hand.append(drawn_card)
            for i in range(handsize):
                drawn_card = self.player_one.draw_card(shuffled_deck)
                self.player_one.cards_in_hand.append(drawn_card)


        count = 0
        draw_count = 8
        current_player = self.get_current_player()
        for i in range(tablesize):
            drawn_card = self.table.draw_card(shuffled_deck)
            if drawn_card.month == 14:
                #print("You can pick up that bonus card cuz you go first!")
                current_player.cards_on_board.append(drawn_card)
                drawn_card = self.table.draw_card(shuffled_deck)
                if drawn_card.month == 14:
                    current_player.cards_on_board.append(drawn_card)
                    drawn_card = self.table.draw_card(shuffled_deck)
                    self.table.cards_on_board.append(drawn_card)
                else:
                    self.table.cards_on_board.append(drawn_card)
            else:
                self.table.cards_on_board.append(drawn_card)



        # sort the cards by month
        # self.player_one.cards_in_hand.sort(key=self.player_one.get_card_month())
        # self.player_two.cards_in_hand.sort(key=self.month)
        # self.table.cards_on_board.sort(key=self.month)

        # sort the cards by month
        self.player_one.cards_in_hand.sort(key=lambda x: x.month)
        self.player_two.cards_in_hand.sort(key=lambda x: x.month)
        self.table.cards_on_board.sort(key=lambda x: x.month)

        # check if there are 4 of the same month in hand - then the player can choose to win the game or play on
        for i in range(0,handsize):
            temp = self.player_one.cards_in_hand[i].month
            month_array_counter_player_one[temp] = month_array_counter_player_one[temp] + 1

        for i in range(1,12):
            if month_array_counter_player_one[i] == 4:
                pass
                #print("There are four of the same month in Player 1's hand, Month", i, "on the table. Would you like to take the free chips?")

        for i in range(0,handsize):
            temp = self.player_two.cards_in_hand[i].month
            month_array_counter_player_two[temp] = month_array_counter_player_two[temp] + 1

        for i in range(1,12):
            if month_array_counter_player_two[i] == 4:
                pass
                #print("There are four of the same month in Player 2's hand, Month", i, "on the table. Would you like to take the free chips?")


        # check if there are 4 of the same month on the board - then the game is replaye
        for i in range(0,tablesize):
            temp = self.table.cards_on_board[i].month
            month_array_counter_communal[temp] = month_array_counter_communal[temp] + 1

        for i in range(1,12):
            if month_array_counter_communal[i] == 4:
                self.game_in_progress = False
                self.replay_game = True
                #print("There are four of the same month on the table, Month", i, "on the table. The game must be replayed for double points!")

        # initialize the turn number
        g.turn_number = 1

        return shuffled_deck

    def roll_to_start(self):
        # test
        x = random.randint(1, 12)
        if x > 6:
            return 1
        else:
            return 2
        # return whoever wins

    def get_current_player(self):
        return self.current_player

    def set_current_player(self, current_player):
        self.current_player = current_player

    def get_current_player_num(self):
        return self.current_player_num

    def set_current_player_num(self, current_player_num):
        self.current_player_num = current_player_num

    def get_waiting_player(self):
        return self.waiting_player

    def set_waiting_player(self, waiting_player):
        self.waiting_player = waiting_player

    def get_waiting_player_num(self):
        return self.waiting_player_num

    def set_waiting_player_num(self, waiting_player_num):
        self.waiting_player_num = waiting_player_num

    def print_player_one_cards(self):
        print()
        print("----------------------------------")
        print("------Player One's Cards--------- ")
        print("----------------------------------")
        for i in self.player_one.cards_in_hand:
            print(i.name, ",", i.month, ",", i.category)

    def print_player_two_cards(self):
        print()
        print("----------------------------------")
        print("------Player Two's Cards----------")
        print("----------------------------------")
        for i in self.player_two.cards_in_hand:
            print(i.name, ",", i.month, ",", i.category)

    def print_player_cards(self, player_num):
        print()
        print("----------------------------------")
        print("------Player", self.get_current_player_num(), "Cards----------")
        print("----------------------------------")
        for i in player_num.cards_in_hand:
            print(i.name, ",", i.month, ",", i.category)

    def print_player_board_cards(self, player_num, player_int):
        print()
        print("----------------------------------")
        print("------Player", player_int, "'s Cards on Board----------")
        print("----------------------------------")
        player_num.cards_on_board.sort(key=lambda x: x.month)
        for i in player_num.cards_on_board:
            print(i.name, ",", i.month, ",", i.category)

    def print_communal_cards(self):
        print()
        print("----------------------------------")
        print("------Cards on the Table----------")
        print("----------------------------------")
        self.table.cards_on_board.sort(key=lambda x: x.month)
        for i in self.table.cards_on_board:
            print(i.name, ",", i.month, ",", i.category)
        print()

    def calc_additional_multipliers(self,player_num_int):
        extra_multiplier = 1

        if player_num_int == 1:
            if self.player_one.gwang_count >= 3 and self.player_two.gwang_count == 0:
                extra_multiplier = extra_multiplier * 2
                #print("Player 1 Gwang Multiplier")
            if self.player_one.gguet_count - self.player_two.gguet_count > 5:
                extra_multiplier = extra_multiplier * 2
                #print("Player 1 Ggeut Multiplier")
            if self.player_one.pi_count > 10 and self.player_two.pi_count < 7:
                extra_multiplier = extra_multiplier * 2
                #print("Player 1 Pi Multiplier")
            if self.player_one.go_count >= 3:
                multiplier = self.player_one.go_count - 2
                extra_multiplier = extra_multiplier * pow(2, multiplier)
            if self.player_two.go_count >= 1:  # if you catch them trying to go for more points you get double points
                #print( "player 1 caught player 2 being greedy. Double points!")
                extra_multiplier = extra_multiplier * 2

        if player_num_int == 2:
            if self.player_two.gwang_count >= 3 and self.player_one.gwang_count == 0:
                extra_multiplier = extra_multiplier * 2
                #print("Player 2 Gwang Multiplier")
            if self.player_two.gguet_count - self.player_one.gguet_count > 5:
                extra_multiplier = extra_multiplier * 2
                #print("Player 2 Ggeut Multiplier")
            if self.player_two.pi_count > 10 and self.player_one.pi_count < 7:
                extra_multiplier = extra_multiplier * 2
                #print("Player 2 Pi Multiplier")
            if self.player_two.go_count >= 3:
                multiplier = self.player_two.go_count - 2
                extra_multiplier = extra_multiplier * pow(2, multiplier)
            if self.player_one.go_count >= 1:  # if you catch them trying to go for more points you get double points
                #print( "player 2 caught player 1 being greedy. Double points!")
                extra_multiplier = extra_multiplier * 2

        return extra_multiplier

    def update_point_total(self, player_num, player_num_int):
        total_overall_points = 0
        total_gwang_points = 0  # brights
        total_gguet_points = 0  # animals
        total_ddi_points = 0  # ribbons
        total_pi_points = 0  # junk
        total_godori_points = 0  # birds
        total_hongdan_points = 0  # red poetry ribbons
        total_cheongdan_points = 0  # blue poetry ribbons
        total_chodan_points = 0  # red ribbons

        gwang_count = 0
        bi_gwang_count = 0
        gguet_count = 0
        ddi_count = 0
        ssang_pi_count = 0
        pi_count = 0
        godori_count = 0
        hongdan_count = 0
        cheongdan_count = 0
        chodan_count = 0
        bonus_two_count = 0
        bonus_three_count = 0
        winning_point_total = 0

        for i in player_num.cards_on_board:
            if i.category == 1:
                gwang_count = gwang_count + 1

                if i.month == 12:
                    bi_gwang_count = 1
            if i.category == 2:
                gguet_count = gguet_count + 1

                if i.month == 2:
                    godori_count = godori_count + 1
                if i.month == 4:
                    godori_count = godori_count + 1
                if i.month == 8:
                    godori_count = godori_count + 1

            if i.category == 3:
                ddi_count = ddi_count + 1

                if i.month == 1:
                    hongdan_count = hongdan_count + 1
                if i.month == 2:
                    hongdan_count = hongdan_count + 1
                if i.month == 3:
                    hongdan_count = hongdan_count + 1

                if i.month == 6:
                    cheongdan_count = cheongdan_count + 1
                if i.month == 9:
                    cheongdan_count = cheongdan_count + 1
                if i.month == 10:
                    cheongdan_count = cheongdan_count + 1

                if i.month == 4:
                    chodan_count = chodan_count + 1
                if i.month == 5:
                    chodan_count = chodan_count + 1
                if i.month == 7:
                    chodan_count = chodan_count + 1

            if i.category == 4:
                pi_count = pi_count + 1

            if i.category == 5:
                ssang_pi_count = ssang_pi_count + 1
                pi_count = pi_count + ssang_pi_count * 2

            if i.category == 7:
                bonus_two_count = bonus_two_count + 1
                pi_count = pi_count + bonus_two_count * 2

            if i.category == 8:
                bonus_three_count = bonus_three_count + 1
                pi_count = pi_count + bonus_three_count * 3

        # total points summary time
        # calculate total gwang points
        if gwang_count == 3:
            if bi_gwang_count == 1:
                total_gwang_points = 2
                #print("Bi Sam Gwang!")
                player_num.gwang_count = 3
            else:
                total_gwang_points = 3
                #print("Sam Gwang!")
                player_num.gwang_count = 3
        elif gwang_count == 4:
            total_gwang_points = 4
            player_num.gwang_count = 4
            #print("Sa Gwang!")
        elif gwang_count == 5:
            total_gwang_points = 15
            player_num.gwang_count = 5
            #print("Oh Gwang!")
        else:
            total_gwang_points = 0

        # calculate total ggeut points


        if godori_count == 3:
            total_gguet_points = total_gguet_points + 5
            #print("Godari!")

        if gguet_count >= 5:
            total_gguet_points = total_gguet_points + gguet_count - 4
            player_num.gguet_count = gguet_count

        # calculate total ddi points
        if hongdan_count == 3:
            total_ddi_points = total_ddi_points + 3
            #print("Hongdan!")
        if cheongdan_count == 3:
            total_ddi_points = total_ddi_points + 3
            #print("Cheongdan!")
        if chodan_count == 3:
            total_ddi_points = total_ddi_points + 3
            #print("Chodan!")
        if ddi_count >= 5:
            total_ddi_points = total_ddi_points + ddi_count - 4

        # calculate total pi points
        if pi_count >= 10:
            total_pi_points = pi_count - 9
            player_num.pi_count = pi_count

        total_overall_points = total_gwang_points + total_gguet_points + total_ddi_points + total_pi_points
        # print(player_local[0].name)
        #print("Player", player_num_int, "has:", total_overall_points, "points")
        #print("gwang_points= ", total_gwang_points, "gguet_points =", total_gguet_points, "ddi points =", total_ddi_points, "pi points =", total_pi_points)

        if self.player_one.ddong_count == 3:
            #print("Player one diarrhea!")
            self.player_one.win = True
            total_overall_points = 5
            return total_overall_points

        if self.player_two.ddong_count == 3:
            #print("Player two diarrhea!")
            self.player_two.win = True
            total_overall_points = 5
            return total_overall_points

        if player_num.go_count == 1:
            total_overall_points = total_overall_points + 1
        if player_num.go_count == 2:
            total_overall_points = total_overall_points + 3



        #print("point multiplier = ", player_num.point_multiplier)
        if total_overall_points >= player_num.required_point_total_to_win:
            #print("We have a winner")

            #user_input = random.randint(1, 3)  # choose either card_one or card_two randomly
            user_input = 1
            if user_input == 2:  # Go!
                self.go_chosen(player_num,player_num_int, total_overall_points)
            else:
                player_num.win = True
                # calc additional multipliers
                extra_multiplier = self.calc_additional_multipliers(player_num_int)
                #print("total overall before = ", total_overall_points)

                total_overall_points = total_overall_points * player_num.point_multiplier * extra_multiplier

                #print("Total over all points = ", total_overall_points, "player_num.point multiplier = ", player_num.point_multiplier, "extra =", extra_multiplier)

                return total_overall_points

        return total_overall_points

    def go_chosen(self, player_num, player_num_int, overall_points):
        #print("Players points at the time of saying go = ", overall_points)

        player_num.go_count = player_num.go_count + 1

        if player_num.go_count == 1:
            player_num.required_point_total_to_win = overall_points + 2
        elif player_num.go_count == 2:
            player_num.required_point_total_to_win = overall_points + 3
        else:
            player_num.required_point_total_to_win = overall_points + 1
        #print("Player", player_num_int, ",", player_num.go_count,"Go!",  "required point total to win = ", player_num.required_point_total_to_win)


    def count_month_in_communal_area(self, the_card):
        month_count = 0
        for i in self.table.cards_on_board:
            if the_card.month == i.month:
                #print("we have a matching month in communal area")
                month_count = month_count + 1

        return month_count

    def count_month_on_my_table(self, the_card, player_num):
        month_count = 0
        for i in player_num.cards_on_board:
            if the_card.month == i.month:
                #print("we have a matching month on table")
                month_count = month_count + 1

        return month_count

    def count_month_in_my_hand(self, the_card, player_num):
        month_count = 0
        for i in player_num.cards_in_hand:
            if the_card.month == i.month:
                #print("we have a matching month in hand")
                month_count = month_count + 1

        return month_count

    '''def steal_pi(self, stealing_player, giving_player):
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
    '''
    #def handle_ppeok_logic(self, player_num, lay_down, drawn_card, bonus_card):


    def add_four_cards_to_players_board(self, player_num, month):
        for i in ALL_CARDS:
            if i.month == month:
                player_num.cards_on_board.append(i)


    def remove_cards_from_players_hand(self, player_num, month):
        for i in player_num.cards_in_hand:
            if i.month == month:
                player_num.cards_in_hand.remove(i)
        for i in player_num.cards_in_hand:
            if i.month == month:
                player_num.cards_in_hand.remove(i)
        for i in player_num.cards_in_hand:
            if i.month == month:
                player_num.cards_in_hand.remove(i)
        for i in player_num.cards_in_hand:
            if i.month == month:
                player_num.cards_in_hand.remove(i)


    def remove_cards_from_communal_area(self, month):
        for i in self.table.cards_on_board:
            if i.month == month:
                self.table.cards_on_board.remove(i)
        for i in self.table.cards_on_board:
            if i.month == month:
                self.table.cards_on_board.remove(i)
        for i in self.table.cards_on_board:
            if i.month == month:
                self.table.cards_on_board.remove(i)
        for i in self.table.cards_on_board:
            if i.month == month:
                self.table.cards_on_board.remove(i)

    def bomb_two(self, lay_down, player_num):
        bomb_two = False

        #print("bomb_two")
        player_num.point_multiplier = player_num.point_multiplier * 2
        bomb_two = True
        # create one bomb card
        bomb_card = Card('Bomb', 13, 6, Images.CRANE_GIF)

        player_num.cards_in_hand.append(bomb_card)

        #add all four cards of the lay_down month to the player's board
        self.add_four_cards_to_players_board(player_num, lay_down.month)
        #remove all four cards from the hand and table
        self.remove_cards_from_players_hand(player_num, lay_down.month)
        self.remove_cards_from_communal_area(lay_down.month)
        player_num.steal_pi(player_num, self.get_waiting_player())


        return bomb_two

    def bomb_three(self, lay_down, player_num):
        bomb_three = False

        #print("bomb_three")
        player_num.point_multiplier = player_num.point_multiplier * 2
        bomb_three = True
        # create two bomb cards
        bomb_card = Card('Bomb', 13, 6, Images.CRANE_GIF)
        player_num.cards_in_hand.append(bomb_card)
        bomb_card = Card('Bomb', 13, 6, Images.CRANE_GIF)
        player_num.cards_in_hand.append(bomb_card)

        #add all four cards of the lay_down month to the player's board
        self.add_four_cards_to_players_board(player_num, lay_down.month)
        #remove all four cards from the hand and table
        self.remove_cards_from_players_hand(player_num, lay_down.month)
        self.remove_cards_from_communal_area(lay_down.month)
        player_num.steal_pi(player_num, self.get_waiting_player())


        return bomb_three

    def shake_three(self, lay_down, player_num):
        shake_three = False

        #print("shake_three")
        player_num.point_multiplier = player_num.point_multiplier * 2
        shake_three = True
        return shake_three

    def shake_four(self, lay_down, player_num):
        shake_four = False

        #print("shake_four")
        player_num.point_multiplier = player_num.point_multiplier * 2
        shake_four = True
        return shake_four

    def check_for_complete_month(self, the_card, player_num):
        complete_month = False

        #print("Lucky you! You completed a month")
        current_player_num_local = self.get_current_player_num()
        current_player_local = self.get_current_player()

        #print("The current player num is", current_player_num_local)

        complete_month = True

        # append all four cards from lay_down month to the player's board
        for i in self.table.cards_on_board:
            if i.month == the_card.month:
                player_num.cards_on_board.append(i)

        for i in self.table.cards_on_board:
            if i.month == the_card.month:
                self.table.cards_on_board.remove(i)
        for i in self.table.cards_on_board:
            if i.month == the_card.month:
                self.table.cards_on_board.remove(i)
        for i in self.table.cards_on_board:
            if i.month == the_card.month:
                self.table.cards_on_board.remove(i)
        for i in self.table.cards_on_board:
            if i.month == the_card.month:
                self.table.cards_on_board.remove(i)

        #print("the card is", the_card.name)

        #for i in player_num.ddong_month:
        for i in player_num.ddong_month:

            if i == the_card.month:
                #print("ja-ppuk! Stealing two PI cards")
                player_num.steal_pi(player_num, self.get_waiting_player())
                player_num.ddong_month.remove(i)

            else:
                #print("bi shi")
                pass

        player_num.steal_pi(player_num, self.get_waiting_player())

        if self.bonus_ddong_association_month_one == the_card.month:
            #print("Pick up the 1st bonus card via association, too")
            player_num.cards_on_board.append(self.bonus_card_first)
            #self.print_player_board_cards(player_num,4)
            self.table.cards_on_board.remove(self.bonus_card_first)
            #self.bonus_ddong_association_month_one = 0 # reset this value
            player_num.steal_pi(player_num, self.get_waiting_player())
            #self.print_communal_cards()
        elif self.bonus_ddong_association_month_two == the_card.month:
            #print("Pick up the 2nd bonus card via association, too")
            player_num.cards_on_board.append(self.bonus_card_second)
            #self.print_player_board_cards(player_num,4)
            self.table.cards_on_board.remove(self.bonus_card_second)
            #self.bonus_ddong_association_month_two = 0 # reset this value
            player_num.steal_pi(player_num, self.get_waiting_player())
            #self.print_communal_cards()
        else:
            pass


        return complete_month

    def check_for_need_to_choose_card(self, the_card, player_num, lay_bool):
        need_to_choose_card = False
        user_input = 0

        # print("You need to choose from one of the two cards")
        need_to_choose_card = True

        # print("The month is", the_card.month)
        card_one = the_card  # just temporary
        card_two = the_card  # just temporary

        first_card_count = 0
        for i in self.table.cards_on_board:
            if first_card_count == 0 and i.month == the_card.month:
                card_one = i
                first_card_count = 1
            elif first_card_count == 1 and i.month == the_card.month:
                card_two = i
                first_card_count = 2

        user_input = random.randint(1, 3)  # choose either card_one or card_two randomly

        # need to move the lay_card and chosen card to players board for points
        if user_input == 1:
            player_num.cards_on_board.append(card_one)
            self.table.cards_on_board.remove(card_one)

        else:
            player_num.cards_on_board.append(card_two)
            self.table.cards_on_board.remove(card_two)

        player_num.cards_on_board.append(the_card)
        if lay_bool:
            self.table.cards_on_board.remove(the_card)

        # now, remove lay_card and chosen card from



        return need_to_choose_card

    def check_for_card_match(self, lay_down, player_num):
        card_match = False

        #print("You matched a single card")
        card_match = True

        for i in self.table.cards_on_board:
            if i.month == lay_down.month:
                player_num.cards_on_board.append(i)
                #print("appended one")

        self.table.cards_on_board.remove(lay_down)

        for i in self.table.cards_on_board:
            if i.month == lay_down.month:
                #print("found one")
                # just_in_case_card = i
                self.table.cards_on_board.remove(i)

        # return just_in_case_card


    def test_button(self, input_local):
        print(input_local)

    def set_starting_player(self, first_to_act):

        if first_to_act == 1:
            #print("Congratulations, Player 1. You will start!")
            self.set_current_player(self.player_one)
            self.set_current_player_num(1)
            self.set_waiting_player(self.player_two)
            self.set_waiting_player_num(2)
        else:
            #print("Congratulations, Player 2. You will start!")
            self.set_current_player(self.player_two)
            self.set_current_player_num(2)
            self.set_waiting_player(self.player_one)
            self.set_waiting_player_num(1)


    def bonus_card_checker(self):
        pass

    def add_card_to_gui(self, player_one_hand, player_one_board, player_two_hand, player_two_board, communal_cards):
        pass

    def update_gui(self, player_one_hand, player_one_board, player_two_hand, player_two_board, communal_cards):

        #win = Tk()
        #window = Tk()

        #if not bFirst:
            #window = Tk()

        window_width = 1600
        window_height = 1000

        # get the screen dimension
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        #window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        window.title("Hi Jihye!")
        #frame = Frame(master=window, width=50, height=50)

        window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=100, weight=1)
        window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=100, weight=1)

        player_one_card_list = []
        player_two_card_list = []
        communal_cards_list = []
        player_one_board_list = []
        player_two_board_list = []

        count = 0
        for i in player_one_hand:
            the_card = i
            #card_button_player_one = ttk.Button(master=window, image=i.image, command=lambda the_card=the_card: self.player_one.lay_down_chosen_card(self.player_one.cards_in_hand, the_card, player_one_card_list, card_button_player_one))
            card_button_player_one = ttk.Button(master=window, image=i.image)
            card_button_player_one['command'] = lambda the_card=the_card, button_inst = card_button_player_one: self.player_one.lay_down_chosen_card(self.player_one.cards_in_hand, the_card, player_one_card_list, button_inst)
            player_one_card_list.append(card_button_player_one)
            player_one_card_list[count].grid(row=10, column=count, sticky="nsew")
            count = count + 1

        count = 0
        for i in player_two_hand:
            card_button_player_two = ttk.Button(master=window, image=i.image, command=self.player_one.test_two)
            player_two_card_list.append(card_button_player_two)
            #button_array[count].pack(side=LEFT)
            player_two_card_list[count].grid(row=0, column=count, sticky="nsew")
            count = count + 1

        count = 0
        for i in communal_cards:
            the_card = i
            #card_button_communal = ttk.Button(master=window, image=i.image, command=self.player_one.test_two())
            label_communal = ttk.Label(master=window, image=i.image)
            #card_button = ttk.Button(master=window, image=i.image, command=lambda the_card=the_card: self.player_one.lay_down_chosen_card(self.player_one.cards_in_hand,the_card))
            communal_cards_list.append(label_communal)
            communal_cards_list[count].grid(row=5, column=count, sticky="nsew")
            count = count + 1

        '''
        count = 0
        for i in player_one_board:
            the_card = i
            label_player_one_board = ttk.Button(master=window, image=i.image)
            player_one_board_list.append(label_player_one_board)
            player_one_board_list[count].grid(row=8, column=count, sticky="nsew")
            count = count + 1

        count = 0
        for i in player_two_board:
            the_card = i
            label_player_two_board = ttk.Button(master=window, image=i.image)
            player_two_board_list.append(label_player_two_board)
            player_two_board_list[count].grid(row=2, column=count, sticky="nsew")
            count = count + 1
        '''

        window.destroy()
        window.mainloop()

    '''def play_against_ai(self, shuffled_deck):
    #def simulate_game(self, first_to_act):


        # print("\nPlayer", self.get_current_player_num(), "'s turn! Select Card to Play!")

        # wait for the player to play a card.
        current_player = self.get_current_player()
        current_player_num = self.get_current_player_num()
        waiting_player = self.get_waiting_player()
        waiting_player_num = self.get_waiting_player_num()
        ppeok_bool = False


        #def lay_down_chosen_card(self, cards_in_hand, the_card, card_list, card_button):

        lay_down = self.current_player.lay_down_random_card(self.current_player.cards_in_hand)
        # print("Player", current_player_num, "played: ", lay_down.name, ",", lay_down.month, ",", lay_down.category)

        if lay_down.month == 14:
            while lay_down.month == 14:
                self.current_player.cards_on_board.append(lay_down)
                replacement_card = self.current_player.draw_card(shuffled_deck)
                self.current_player.cards_in_hand.append(replacement_card)
                lay_down = self.current_player.lay_down_random_card(self.current_player.cards_in_hand)
                self.steal_pi(current_player, waiting_player)
                print("stole a pi using bonus card")

        drawn_card = self.table.draw_card(shuffled_deck)
        bonus_card = drawn_card
        if drawn_card.month == 14:
            while drawn_card.month == 14:
                self.current_player.cards_on_board.append(drawn_card)
                bonus_card = drawn_card
                drawn_card = self.table.draw_card(shuffled_deck)

                if lay_down.month == drawn_card.month:
                    print("ppeok!")
                    ppeok_bool = True
                    self.steal_pi(current_player, waiting_player)  # remove later
                else:
                    self.steal_pi(current_player, waiting_player)

        # print("Player", current_player_num, "draw card is: ", drawn_card.name, ",", drawn_card.month, ",", drawn_card.category)

        just_in_case_card = lay_down

        # add it to the table
        if lay_down.category != 6:

            self.table.cards_on_board.append(lay_down)
        else:
            pass
            # print("Bomb was played, but not appended to the table")

        # self.print_communal_cards()

        # matching_count = self.check_for_match_on_play(lay_down)

        month_count_in_communal_area_lay_down = self.count_month_in_communal_area(lay_down)
        month_count_on_my_table_lay_down = self.count_month_on_my_table(lay_down, current_player)
        month_count_in_my_hand_lay_down = self.count_month_in_my_hand(lay_down, current_player)

        # print("Month count in communal area lay down= ", month_count_in_communal_area_lay_down)
        # print("Month count on my table lay down = ", month_count_on_my_table_lay_down)
        # print("Month count in my hand lay down = ", month_count_in_my_hand_lay_down)

        month_count_in_communal_area_drawn = self.count_month_in_communal_area(drawn_card)
        month_count_on_my_table_drawn = self.count_month_on_my_table(drawn_card, current_player)
        month_count_in_my_hand_drawn = self.count_month_in_my_hand(drawn_card, current_player)

        # print("Month count in communal area drawn = ", month_count_in_communal_area_drawn)
        # print("Month count on my table drawn = ", month_count_on_my_table_drawn)
        # print("Month count in my hand drawn = ", month_count_in_my_hand_drawn)

        # if ppeok_bool:
        #    self.handle_ppeok_logic(current_player, lay_down, drawn_card, bonus_card)
        if month_count_in_communal_area_lay_down == 3 and month_count_in_my_hand_lay_down == 1:
            bomb_two = self.check_for_bomb_two(lay_down, current_player)
        elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 2:
            bomb_three = self.check_for_bomb_three(lay_down, current_player)
        elif month_count_in_communal_area_lay_down == 1 and month_count_in_my_hand_lay_down == 2:
            shake_three = self.check_for_shake_three(lay_down, current_player)
        elif month_count_in_communal_area_lay_down == 1 and month_count_in_my_hand_lay_down == 3:
            shake_four = self.check_for_shake_four(lay_down, current_player)
        elif month_count_in_communal_area_lay_down == 4 and month_count_in_my_hand_lay_down == 0:
            print("check the other one")
            complete_month = self.check_for_complete_month(lay_down, current_player)
        elif month_count_in_communal_area_lay_down == 3 and month_count_in_my_hand_lay_down == 0:
            need_to_choose_card = self.check_for_need_to_choose_card(lay_down, current_player, True)
        elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 0:
            just_in_case_card = self.check_for_card_match(lay_down, current_player, just_in_case_card)
        elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 1:
            just_in_case_card = self.check_for_card_match(lay_down, current_player, just_in_case_card)
        else:
            pass
            # print("You swung and missed!")

        # lets do draw card logic here
        self.check_drawn_card_logic(current_player, lay_down, drawn_card, month_count_in_communal_area_drawn,
                                    month_count_in_my_hand_drawn, just_in_case_card)

        # ppeok_bool = False

        point_total_player_one = self.update_point_total(self.player_one, 1)
        point_total_player_two = self.update_point_total(self.player_two, 2)

        if self.player_one.win:
            # self.print_player_board_cards(self.player_one, 1)
            # self.print_player_board_cards(self.player_two, 2)
            # print("Player 1 wins with ", point_total_player_one, "points")
            return point_total_player_one
        elif self.player_two.win:
            # self.print_player_board_cards(self.player_one, 1)
            # self.print_player_board_cards(self.player_two, 2)
            # print("Player 2 wins with ", point_total_player_two, "points")
            return -point_total_player_two
        else:
            pass

        size_of_hand_player_one = len(self.player_one.cards_in_hand)
        size_of_hand_player_two = len(self.player_two.cards_in_hand)

        if self.get_current_player_num() == 1:
            self.set_current_player_num(2)
            self.set_current_player(self.player_two)
            self.set_waiting_player(self.player_one)
            self.set_waiting_player_num(1)
        else:
            self.set_current_player_num(1)
            self.set_current_player(self.player_one)
            self.set_waiting_player(self.player_two)
            self.set_waiting_player_num(2)

        if size_of_hand_player_one == 0 and size_of_hand_player_two == 0:
            still_playing = False
            print("Nagari! Play again")
            # print("Player 1 had ", point_total_player_one, "points")
            # print("Player 2 had ", point_total_player_two, "points")
            # print("Player", self.get_current_player_num(), "is out of cards!")

        # self.print_player_one_cards()
        # self.print_player_two_cards()
        # self.print_communal_cards()

        # self.print_player_board_cards(self.player_one, 1)
        # self.print_player_board_cards(self.player_two, 2)

        return 0  # returns a tied game
    '''
    def start_cycle(self, cards_in_hand, the_card, card_list_card_button):
        pass

    def evaluate_communal_board_state(self, player_num, lay_down_card, drawn_card, ppeok_bool, bonus_card):

        # 1: count the cards that match the month of played card and drawn card
        month_count_in_communal_area_lay_down = self.count_month_in_communal_area(lay_down_card)
        month_count_on_my_table_lay_down = self.count_month_on_my_table(lay_down_card, player_num)
        month_count_in_my_hand_lay_down = self.count_month_in_my_hand(lay_down_card, player_num)
        month_count_in_communal_area_drawn = self.count_month_in_communal_area(drawn_card)
        month_count_on_my_table_drawn = self.count_month_on_my_table(drawn_card, player_num)
        month_count_in_my_hand_drawn = self.count_month_in_my_hand(drawn_card, player_num)

        #print("month count in communal area lay down : ", month_count_in_communal_area_lay_down)
        #print("month month_count_on_my_table_lay_down : ", month_count_on_my_table_lay_down)
        #print("month_count_in_my_hand_lay_down : ", month_count_in_my_hand_lay_down)
        #print("month_count_in_communal_area_drawn : ", month_count_in_communal_area_drawn)
        #print("month_count_on_my_table_drawn: ", month_count_on_my_table_drawn)
        #print("month_count_in_my_hand_drawn: ", month_count_in_my_hand_drawn)

        if lay_down_card.month == drawn_card.month:
            # 1. if they are the only two cards there, then its a miracle pluck and we'll steal a card
            if month_count_in_communal_area_lay_down == 2:
                #print("Jjok!")
                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        player_num.cards_on_board.append(i)
                        self.table.cards_on_board.remove(i)
                player_num.cards_on_board.append(drawn_card)
                player_num.steal_pi(player_num, self.get_waiting_player())
                if ppeok_bool:
                    player_num.cards_on_board.append(bonus_card)
                    self.table.cards_on_board.remove(bonus_card)

        # 2. if there are three cards there then its a ddong
            elif month_count_in_communal_area_lay_down == 3:
                #print("DDong!!")
                player_num.ddong_count = player_num.ddong_count + 1
                player_num.ddong_month.append(drawn_card.month)

                if self.turn_number == 1: # if the first turn for the 1st player.
                    self.current_player.first_turn_ddong = True
                if self.turn_number == 1.5: #if its the first turn for the 2nd player.
                    self.current_player.first_turn_ddong = True

                if ppeok_bool:
                    #print("Bonus card not acquired because its stuck in ddong")
                    if self.bonus_ddong_association_month_one == 0:
                        self.bonus_ddong_association_month_one = drawn_card.month
                        self.bonus_card_first = bonus_card
                    else:
                        self.bonus_ddong_association_month_two = drawn_card.month
                        self.bonus_card_second = bonus_card

        # 3. if there are four cards there, then we're picking them all up and stealing a card
            elif month_count_in_communal_area_lay_down == 4:
                #print("Ddadak!!")
                self.add_four_cards_to_players_board(player_num, drawn_card.month)
                self.remove_cards_from_communal_area(drawn_card.month)
                player_num.steal_pi(player_num, self.get_waiting_player())

                if player_num.ddong_month == drawn_card.month:
                    #print("Stealing another one acquired for my ddadak")
                    player_num.steal_pi(player_num, self.get_waiting_player())

                if ppeok_bool:
                    player_num.cards_on_board.append(bonus_card)
                    self.table.cards_on_board.remove(bonus_card)
                    #print("Stealing from bonus card acquired through ddaddak ")
                    player_num.steal_pi(player_num, self.get_waiting_player())
            else:
                print("Bug in laydown = draw card logic")
                pass

        else:

            if month_count_in_communal_area_drawn == 0:
                #print("Case -1 - strange, it shouldn't be possible")
                pass
            elif month_count_in_communal_area_drawn == 1:
                #print("Case 0 - no match of drawn card")
                pass

            elif month_count_in_communal_area_drawn == 2:
                # put both cards in the players board
                #print("Case 1 - Matched one on the flip-up!")

                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        player_num.cards_on_board.append(i)
                #player_num.cards_on_board.append(drawn_card)

                # check for Sseul event : Only two cards are on the map, and then the played and drawn card's months match those two.
                if month_count_in_communal_area_lay_down == 2 and len(self.table.cards_on_board) == 4:
                    #print("Sseul!")
                    player_num.steal_pi(player_num, self.get_waiting_player())

                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        self.table.cards_on_board.remove(i)
                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        self.table.cards_on_board.remove(i)
                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        self.table.cards_on_board.remove(i)

            elif month_count_in_communal_area_drawn == 3:
                #print("Case 2 - need to choose from the two cards")

                self.check_for_need_to_choose_card(drawn_card, player_num, False)

            elif month_count_in_communal_area_drawn == 4:
                #print("Case 3 - Wow we're collecting them all!")
                self.check_for_complete_month(drawn_card, player_num)

            else:
                print("Bug in the logic :(")
                pass


            # 2: Check for bomb_two
            if month_count_in_communal_area_lay_down == 3 and month_count_in_my_hand_lay_down == 1:
                bomb_two = self.bomb_two(lay_down_card, player_num)
                #print("bomb two")
            # 3: Check for bomb_three
            elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 2:
                bomb_three = self.bomb_three(lay_down_card, player_num)
                #print("bomb three")
            # 4: Check for shake_three
            elif month_count_in_communal_area_lay_down == 1 and month_count_in_my_hand_lay_down == 2:
                shake_three = self.shake_three(lay_down_card, player_num)
                #print("shake_three")
            # 5: Check for shake_four
            elif month_count_in_communal_area_lay_down == 1 and month_count_in_my_hand_lay_down == 3:
                shake_four = self.shake_four(lay_down_card, player_num)
                #print("shake_four")
            # 6: check for complete month
            elif month_count_in_communal_area_lay_down == 4 and month_count_in_my_hand_lay_down == 0:
                #print("gets here to complete month")
                complete_month = self.check_for_complete_month(lay_down_card, player_num)
            # 7: check for choose from two cards
            elif month_count_in_communal_area_lay_down == 3 and month_count_in_my_hand_lay_down == 0:
                need_to_choose_card = self.check_for_need_to_choose_card(lay_down_card, player_num, True)
                #print("choose card")
            # 8: check for card match
            elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 0:
                just_in_case_card = self.check_for_card_match(lay_down_card, player_num)
                #print("played card has a match")
            elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 1:
                just_in_case_card = self.check_for_card_match(lay_down_card, player_num)
                #print("played card has a match")
            else:
                pass
                #print("No match of played card!")


    def simulate_game(self, first_to_act):

        # setup the game
        shuffled_deck = self.setup_game(first_to_act)

        #self.update_gui(self.player_one.cards_in_hand, self.player_one.cards_on_board, self.player_two.cards_in_hand,
        #                self.player_two.cards_on_board, self.table.cards_on_board)
        #self.print_player_one_cards()
        #self.print_player_two_cards()
        #self.print_communal_cards()

        #still_playing = True


        while self.game_in_progress:

            # wait for the player to play a card.
            current_player = self.get_current_player()
            current_player_num = self.get_current_player_num()
            waiting_player = self.get_waiting_player()
            waiting_player_num = self.get_waiting_player_num()
            ppeok_bool = False

            # lay down logic
            lay_down = self.current_player.lay_down_random_card(self.current_player.cards_in_hand, shuffled_deck, current_player, waiting_player)
            #print("Player", current_player_num, "played: ", lay_down.name, ",", lay_down.month, ",", lay_down.category)

            #just_in_case_card = lay_down # this is just a temporary declaration

            # add it to the table
            if lay_down.category != 6:

                self.table.cards_on_board.append(lay_down)
            else:
                #print("Bomb was played, but not appended to the table")
                pass

            drawn_card = self.table.draw_card(shuffled_deck)
            # bonus_card = drawn_card
            if drawn_card.month == 14:

                self.bonus_temp_card = drawn_card
                while drawn_card.month == 14:
                    # puts the bonus card into the players board
                    self.current_player.cards_on_board.append(drawn_card)

                    drawn_card = self.table.draw_card(shuffled_deck)

                if lay_down.month == drawn_card.month:
                    #print("ppeok, ddong, miracle chance!")
                    ppeok_bool = True
                    if not self.bonus_bool:
                        self.bonus_card_first = self.bonus_temp_card
                        self.table.cards_on_board.append(self.bonus_card_first)
                        self.table.cards_on_board.append(drawn_card)
                        self.current_player.cards_on_board.remove(self.bonus_card_first)
                        self.evaluate_communal_board_state(current_player, lay_down, drawn_card, ppeok_bool, self.bonus_card_first)
                        self.bonus_bool = True
                    elif self.bonus_bool:
                        self.bonus_card_second = self.bonus_temp_card
                        self.table.cards_on_board.append(self.bonus_card_second)
                        self.table.cards_on_board.append(drawn_card)
                        self.current_player.cards_on_board.remove(self.bonus_card_second)
                        self.evaluate_communal_board_state(current_player, lay_down, drawn_card, ppeok_bool, self.bonus_card_second)
                    else:
                        print("buggy lolo")
                        pass
                    #current_player.steal_pi(current_player, waiting_player)  # remove later

                else:
                    current_player.steal_pi(current_player, waiting_player)
                    ppeok_bool = False

            if ppeok_bool:
                pass
            else:
                self.table.cards_on_board.append(drawn_card)
                self.evaluate_communal_board_state(current_player, lay_down, drawn_card, ppeok_bool, self.bonus_card_first)

            #self.evaluate_communal_board_state(current_player, lay_down, drawn_card, ppeok_bool, self.bonus_card_first)

            # lets do draw card logic here
            #self.check_drawn_card_logic(current_player, lay_down, drawn_card, month_count_in_communal_area_drawn, month_count_in_my_hand_drawn, just_in_case_card)

            point_total_player_one = self.update_point_total(self.player_one, 1)
            point_total_player_two = self.update_point_total(self.player_two, 2)

            if self.player_one.win:
                #self.print_player_board_cards(self.player_one, 1)
                #self.print_player_board_cards(self.player_two, 2)
                #print("Player 1 wins with ", point_total_player_one, "points")
                return point_total_player_one
            elif self.player_two.win:
                #self.print_player_board_cards(self.player_one, 1)
                #self.print_player_board_cards(self.player_two, 2)
                #print("Player 2 wins with ", point_total_player_two, "points")
                return -point_total_player_two
            else:
                pass

            size_of_hand_player_one = len(self.player_one.cards_in_hand)
            size_of_hand_player_two = len(self.player_two.cards_in_hand)

            if self.get_current_player_num() == 1:
                self.set_current_player_num(2)
                self.set_current_player(self.player_two)
                self.set_waiting_player(self.player_one)
                self.set_waiting_player_num(1)
            else:
                self.set_current_player_num(1)
                self.set_current_player(self.player_one)
                self.set_waiting_player(self.player_two)
                self.set_waiting_player_num(2)

            self.turn_number = self.turn_number + .5

            if size_of_hand_player_one == 0 and size_of_hand_player_two == 0:
                self.game_in_progress = False
                #print("Nagari! Play again - this time the game will be played for double points!")
                #print("Player 1 had ", point_total_player_one, "points")
                #print("Player 2 had ", point_total_player_two, "points")
                #print("Player", self.get_current_player_num(), "is out of cards!")

        return 0  # returns a tied game


# initialize vars
game_num = 0
player_one_win_count = 0
player_two_win_count = 0
player_one_point_total = 0
player_two_point_total = 0
player_one_money_won = 0
player_two_money_won = 0
tie_count = 0
winner = 0
who_goes_first = 0
turn_count_array = []
time_array = []

while game_num < 1000:
    start = time.time()

    g = Game()
    if game_num == 0:
        who_goes_first = g.roll_to_start()
    else:
        if winner > 0:
            who_goes_first = 1
        elif winner < 0:
            who_goes_first = 2
        else:
            pass

    #g.draw_gui()

    winner = g.simulate_game(who_goes_first)
    #winner = g.simulate_game(1)
    if winner > 0:
        player_one_win_count = player_one_win_count + 1
    elif winner < 0:
        player_two_win_count = player_two_win_count + 1
    elif winner == 0 and g.replay_game:
        game_num = game_num - 1
    else:
        tie_count = tie_count + 1

    if g.player_one.first_turn_ddong:
        player_one_point_total = player_one_point_total + 3
        player_two_point_total = player_two_point_total - 3
        #print("Player two gave 3 chips to player one")
    if g.player_two.first_turn_ddong:
        player_one_point_total = player_one_point_total - 3
        player_two_point_total = player_two_point_total + 3
        #print("Player one gave 3 chips to player two")
    player_one_point_total = player_one_point_total + winner
    player_two_point_total = player_two_point_total - winner
    game_num = game_num + 1
    turn_count_array.append(g.turn_number)

    end = time.time()
    time_array.append(end-start)
    #print("The game completed in", g.turn_number, "turns")


player_one_money_total = player_one_point_total * 100
player_two_money_total = player_two_point_total * 100

#for i in turn_count_array:
#    print(i)
#for i in time_array:
#    print(i)

print("The average turns is: ", sum(turn_count_array) / len(turn_count_array))
print("The average time is: ", sum(time_array) / len(time_array))

print("Total Games Played:", game_num)
print("Player 1 Games Won:", player_one_win_count)
print("Player 2 Games Won:", player_two_win_count)
print("Tied games: ", tie_count)

print("Player 1 Net Points:", player_one_point_total)
print("Player 2 Net Points:", player_two_point_total)

print("Player 1 Net Money:", player_one_money_total)
print("Player 2 Net Points:", player_two_money_total)

print("Game finished successfully")
