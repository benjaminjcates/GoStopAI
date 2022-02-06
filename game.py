import random
from deck import Deck
from player import Player
from card import Card
from card import ALL_CARDS
from player import HandOfCards


class Game:
    def __init__(self):
        print()
        self.deck = Deck()
        self.player_one = Player(True, self.deck)
        self.player_two = Player(False, self.deck)
        self.table = Player(False, self.deck)

    def setup_game(self):
        # create a new deck
        new_deck = self.deck.create_deck(ALL_CARDS)

        # shuffle the deck
        shuffled_deck = self.deck.shuffle(new_deck)

        # print the shuffled deck in order
        #for c in shuffled_deck:
            #print(c.name, c.month, c.category)

        length = self.deck.deck_size(shuffled_deck)
        #print("The # of remaining cards before pop is " + str(length))
        # drawn_card = self.deck.draw_card(new_deck)

        #deal out all the cards
        for i in range(10):
            drawn_card = self.player_one.draw_card(shuffled_deck)
            self.player_one.cards_in_hand.append(drawn_card)

        for i in range(10):
            drawn_card = self.player_two.draw_card(shuffled_deck)
            self.player_two.cards_in_hand.append(drawn_card)

        for i in range(8):
            drawn_card = self.table.draw_card(shuffled_deck)
            self.table.cards_on_board.append(drawn_card)

        #sort the cards by month
        #self.player_one.cards_in_hand.sort(key=self.player_one.get_card_month())
        #self.player_two.cards_in_hand.sort(key=self.month)
        #self.table.cards_on_board.sort(key=self.month)

        #sort the cards by month
        self.player_one.cards_in_hand.sort(key=lambda x: x.month)
        self.player_two.cards_in_hand.sort(key=lambda x: x.month)
        self.table.cards_on_board.sort(key=lambda x: x.month)

    def roll_to_start(self):
        x = random.randint(1, 12)
        if x > 6:
            return 1
        else:
            return 0
        # return whoever wins

    def play_game(self, first_to_act):

        #run this once to set up the game
        self.setup_game()

        #player_one_hand = self.player_one.cards
        #player_two_hand = self.player_two.cards

        #player_one_hand = HandOfCards.get_hand_of_cards(self.player_one)
        #player_two_hand = HandOfCards.get_hand_of_cards(self.player_two)

        if first_to_act == 1:
            print("Congratulations, Player 1. You will start!")
        else:
            print("Congratulations, Player 2. You will start!")

        print("----------------------------------")
        print("------Player One's Cards--------- ")
        print("----------------------------------")

        #for i in player_one_hand:
        for i in self.player_one.cards_in_hand:
            print(i.name, ",", i.month, ",", i.category)


        #print(self.player_one.cards_in_hand.name)
        print()
        print("----------------------------------")
        print("------Player Two's Cards----------")
        print("----------------------------------")

        for i in self.player_two.cards_in_hand:
            print(i.name, ",", i.month, ",", i.category)

        print()
        print("----------------------------------")
        print("------Cards on the Table----------")
        print("----------------------------------")

        for i in self.table.cards_on_board:
            print(i.name, ",", i.month, ",", i.category)

        #rolls to decide which player gets to start
        #determine who is first to act, then give then have them play a random card





g = Game()
who_goes_first = g.roll_to_start()
g.play_game(who_goes_first)
