import random
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

    def setup_game(self, first_to_act):
        # create a new deck
        new_deck = self.deck.create_deck(ALL_CARDS)

        # shuffle the deck
        shuffled_deck = self.deck.shuffle(new_deck)

        # print the shuffled deck in order
        # for c in shuffled_deck:
        # print(c.name, c.month, c.category)

        length = self.deck.deck_size(shuffled_deck)
        # print("The # of remaining cards before pop is " + str(length))
        # drawn_card = self.deck.draw_card(new_deck)

        # deal out all the cards
        for i in range(10):
            drawn_card = self.player_one.draw_card(shuffled_deck)
            self.player_one.cards_in_hand.append(drawn_card)

        for i in range(10):
            drawn_card = self.player_two.draw_card(shuffled_deck)
            self.player_two.cards_in_hand.append(drawn_card)

        count = 0
        draw_count = 8
        current_player = self.get_current_player()
        for i in range(draw_count):
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

        # set the starting and waiting player
        self.set_starting_player(first_to_act)

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


        #print("point multiplier = ", player_num.point_multiplier)
        if total_overall_points >= 7:
            #print("We have a winner")
            player_num.win = True
            # calc additional multipliers
            extra_multiplier = self.calc_additional_multipliers(player_num_int)
            #print("total overall before = ", total_overall_points)

            total_overall_points = total_overall_points * player_num.point_multiplier * extra_multiplier



            #print("Total over all points = ", total_overall_points, "player_num.point multiplier = ", player_num.point_multiplier, "extra =", extra_multiplier)

            return total_overall_points

        return total_overall_points

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

    def check_for_bomb_two(self, lay_down, player_num):
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
        self.steal_pi(player_num, self.get_waiting_player())


        return bomb_two

    def check_for_bomb_three(self, lay_down, player_num):
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
        self.steal_pi(player_num, self.get_waiting_player())


        return bomb_three

    def check_for_shake_three(self, lay_down, player_num):
        shake_three = False

        #print("shake_three")
        player_num.point_multiplier = player_num.point_multiplier * 2
        shake_three = True
        return shake_three

    def check_for_shake_four(self, lay_down, player_num):
        shake_four = False

        #print("shake_four")
        player_num.point_multiplier = player_num.point_multiplier * 2
        shake_four = True
        return shake_four

    def check_for_complete_month(self, the_card, player_num):
        complete_month = False

        print("Lucky you! You completed a month")
        current_player_num_local = self.get_current_player_num()
        current_player_local = self.get_current_player()

        print("The current player num is", current_player_num_local)

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

        print("the card is", the_card.name)

        #for i in player_num.ddong_month:
        for i in player_num.ddong_month:

            if i == the_card.month:
                print("ja-ppuk! Stealing two PI cards")
                self.steal_pi(player_num, self.get_waiting_player())
                player_num.ddong_month.remove(i)

            else:
                print("bi shi")

        self.steal_pi(player_num, self.get_waiting_player())

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

    def check_for_card_match(self, lay_down, player_num, just_in_case_card):
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
                just_in_case_card = i
                self.table.cards_on_board.remove(i)

        return just_in_case_card

    def check_drawn_card_logic(self, player_num, lay_down, drawn_card, month_count_in_communal_area_drawn, month_count_in_my_hand_drawn, just_in_case_card):
        # if the normal case
        match_count = 0
        if drawn_card.month != lay_down.month:
            if month_count_in_communal_area_drawn == 0:
                self.table.cards_on_board.append(drawn_card)
                #print("Case 0")

            elif month_count_in_communal_area_drawn == 1:
                # put both cards in the players board
                #print("Case 1 - Matched one on the flip-up!")

                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        player_num.cards_on_board.append(i)

                player_num.cards_on_board.append(drawn_card)

                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        #print("removed balls 1")
                        self.table.cards_on_board.remove(i)
                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        print("removed balls 2")
                        self.table.cards_on_board.remove(i)

            elif month_count_in_communal_area_drawn == 2:
                #print("Case 2 - need to choose from the two cards")

                self.check_for_need_to_choose_card(drawn_card, player_num, False)

            elif month_count_in_communal_area_drawn == 3:
                print("Case 3 - Wow we're collecting them all!")

                self.check_for_complete_month(drawn_card, player_num)

            else:
                print("Bug in the logic :(")

        else:
            # 2 possible cases here. Ddadak! and ddong
            if month_count_in_communal_area_drawn == 3:
                print("Ddadak!!")
                self.add_four_cards_to_players_board(player_num, drawn_card.month)
                self.remove_cards_from_communal_area(drawn_card.month)
                self.steal_pi(player_num, self.get_waiting_player())
                if player_num.ddong_month == drawn_card.month:
                    print("Stealing another one for ddadak")
                    self.steal_pi(player_num, self.get_waiting_player())

            elif month_count_in_communal_area_drawn == 1:
                print("Jjok!")
                for i in self.table.cards_on_board:
                    if i.month == drawn_card.month:
                        player_num.cards_on_board.append(i)
                        self.table.cards_on_board.remove(i)
                player_num.cards_on_board.append(drawn_card)
                self.steal_pi(player_num, self.get_waiting_player())
            else:
                print("DDong!!")
                self.table.cards_on_board.append(lay_down)
                self.table.cards_on_board.append(drawn_card)
                self.table.cards_on_board.append(just_in_case_card)
                player_num.ddong_count = player_num.ddong_count + 1
                player_num.ddong_month.append(drawn_card.month)

                # this corrects the duplication of cards
                for i in player_num.cards_on_board:
                    if i.month == lay_down.month:
                        player_num.cards_on_board.remove(i)
                        print("Removing card 1 from hand")
                for i in player_num.cards_on_board:
                    if i.month == lay_down.month:
                        player_num.cards_on_board.remove(i)
                        print("Removing card 2 from hand")


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

    def evaluate_communal_board_state(self ):
        pass


    def simulate_game(self, first_to_act):

        # setup the game
        shuffled_deck = self.setup_game(first_to_act)

        #self.update_gui(self.player_one.cards_in_hand, self.player_one.cards_on_board, self.player_two.cards_in_hand,
        #                self.player_two.cards_on_board, self.table.cards_on_board)
        #self.print_player_one_cards()
        #self.print_player_two_cards()
        #self.print_communal_cards()

        still_playing = True

        while still_playing:

            # wait for the player to play a card.
            current_player = self.get_current_player()
            current_player_num = self.get_current_player_num()
            waiting_player = self.get_waiting_player()
            waiting_player_num = self.get_waiting_player_num()
            ppeok_bool = False

            # lay down logic
            lay_down = self.current_player.lay_down_random_card(self.current_player.cards_in_hand)
            print("Player", current_player_num, "played: ", lay_down.name, ",", lay_down.month, ",", lay_down.category)

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
                        #print("ppeok!")
                        ppeok_bool = True
                        self.steal_pi(current_player, waiting_player)  # remove later
                    else:
                        self.steal_pi(current_player, waiting_player)

            print("Player", current_player_num, "draw card is: ", drawn_card.name, ",", drawn_card.month, ",", drawn_card.category)

            just_in_case_card = lay_down

            # add it to the table
            if lay_down.category != 6:

                self.table.cards_on_board.append(lay_down)
            else:
                pass
                #print("Bomb was played, but not appended to the table")

            # count the cards that match the month of played card and drawn card
            month_count_in_communal_area_lay_down = self.count_month_in_communal_area(lay_down)
            month_count_on_my_table_lay_down = self.count_month_on_my_table(lay_down, current_player)
            month_count_in_my_hand_lay_down = self.count_month_in_my_hand(lay_down, current_player)
            month_count_in_communal_area_drawn = self.count_month_in_communal_area(drawn_card)
            month_count_on_my_table_drawn = self.count_month_on_my_table(drawn_card, current_player)
            month_count_in_my_hand_drawn = self.count_month_in_my_hand(drawn_card, current_player)

            #if ppeok_bool:
            #    self.handle_ppeok_logic(current_player, lay_down, drawn_card, bonus_card)
            if month_count_in_communal_area_lay_down == 3 and month_count_in_my_hand_lay_down == 1:
                bomb_two = self.check_for_bomb_two(lay_down, current_player)
                print("bomb two")
            elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 2:
                bomb_three = self.check_for_bomb_three(lay_down, current_player)
                print("bomb three")
            elif month_count_in_communal_area_lay_down == 1 and month_count_in_my_hand_lay_down == 2:
                shake_three = self.check_for_shake_three(lay_down, current_player)
                print("shake_three")
            elif month_count_in_communal_area_lay_down == 1 and month_count_in_my_hand_lay_down == 3:
                shake_four = self.check_for_shake_four(lay_down, current_player)
                print("shake_four")
            elif month_count_in_communal_area_lay_down == 4 and month_count_in_my_hand_lay_down == 0:
                print("gets here to complete month")
                complete_month = self.check_for_complete_month(lay_down, current_player)
            elif month_count_in_communal_area_lay_down == 3 and month_count_in_my_hand_lay_down == 0:
                need_to_choose_card = self.check_for_need_to_choose_card(lay_down, current_player, True)
                print("choose card")
            elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 0:
                just_in_case_card = self.check_for_card_match(lay_down, current_player, just_in_case_card)
                print("just in case card 1")
            elif month_count_in_communal_area_lay_down == 2 and month_count_in_my_hand_lay_down == 1:
                just_in_case_card = self.check_for_card_match(lay_down, current_player, just_in_case_card)
                print("just in case card 2")
            else:
                pass
                print("You swung and missed!")





            # lets do draw card logic here
            self.check_drawn_card_logic(current_player, lay_down, drawn_card, month_count_in_communal_area_drawn, month_count_in_my_hand_drawn, just_in_case_card)

            #ppeok_bool = False

            point_total_player_one = self.update_point_total(self.player_one, 1)
            point_total_player_two = self.update_point_total(self.player_two, 2)

            self.print_player_board_cards(self.player_one, 1)
            self.print_player_board_cards(self.player_two, 2)
            self.print_communal_cards()

            #print("point total player one, two = ", point_total_player_one, ",", point_total_player_two)

            if self.player_one.win:
                #self.print_player_board_cards(self.player_one, 1)
                #self.print_player_board_cards(self.player_two, 2)
                print("Player 1 wins with ", point_total_player_one, "points")
                self.turn_number = math.ceil(self.turn_number / 2)
                return point_total_player_one
            elif self.player_two.win:
                #self.print_player_board_cards(self.player_one, 1)
                #self.print_player_board_cards(self.player_two, 2)
                print("Player 2 wins with ", point_total_player_two, "points")
                self.turn_number = math.ceil(self.turn_number / 2)
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

            self.turn_number = self.turn_number + 1

            if size_of_hand_player_one == 0 and size_of_hand_player_two == 0:
                still_playing = False
                print("Nagari! Play again - this time the game will be played for double points!")
                #print("Player 1 had ", point_total_player_one, "points")
                #print("Player 2 had ", point_total_player_two, "points")
                #print("Player", self.get_current_player_num(), "is out of cards!")

        #self.print_player_one_cards()
        #self.print_player_two_cards()
        #self.print_communal_cards()

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

while game_num < 1:
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
    else:
        tie_count = tie_count + 1
    player_one_point_total = player_one_point_total + winner
    player_two_point_total = player_two_point_total - winner
    game_num = game_num + 1
    turn_count_array.append(g.turn_number)

    print("The game completed in", g.turn_number, "turns")


player_one_money_total = player_one_point_total * 100
player_two_money_total = player_two_point_total * 100

for i in turn_count_array:
    print(i)

print("Total Games Played:", game_num)
print("Player 1 Games Won:", player_one_win_count)
print("Player 2 Games Won:", player_two_win_count)
print("Tied games: ", tie_count)

print("Player 1 Net Points:", player_one_point_total)
print("Player 2 Net Points:", player_two_point_total)

print("Player 1 Net Money:", player_one_money_total)
print("Player 2 Net Points:", player_two_money_total)

print("Game finished successfully")
