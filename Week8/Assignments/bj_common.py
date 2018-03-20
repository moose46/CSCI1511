__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: bj_card
    Created: Mar, 19, 2018
    
    Description:
    
===================================================
"""
from card import Card


class BJ_Card(Card):
    """ A black jack card """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


from deck import Deck


class BJ_Deck(Deck):
    """Black jack deck"""

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


from hand import Hand


class BJ_Hand(Hand):
    """A blackjack hand"""

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ':\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

    @property
    def total(self):
        """if a card in the hand has a value of none
        #then total is None"""
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value

        # look for an ace in the hand
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # if hand contains an ace then and total is low enough
        # then treat the ace as 11
        if contains_ace and t <= 11:
            # add on;y ten since we already added one for the ace
            # what if it had two aces?
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


import games


class BJ_Player(BJ_Hand):
    """players hand"""

    def is_hitting(self):
        response = games.ask_yes_no('\n' +
                                    self.name +
                                    ', do you want a hit? [y/n]: ')
        return response == 'y'

    def bust(self):
        print(self.name, "busts.")

    def lose(self):
        print(self.name, 'loses.')

    def win(self):
        print(self.name, 'wins.')

    def push(self):
        print(self.name, 'pushes.')


class BJ_Dealer(BJ_Hand):
    """the dealer"""

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """the game object"""

    def __init__(self, names):
        """

        :param names: a list of names that are playing
        """
        self.players = []
        for name in names:
            self.players.append(BJ_Player(name))

        self.dealer = BJ_Dealer('Dealer')

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        """pp. 280"""
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __aditional_cards(self, player):
        """

        :param player:
        :return:
        """
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        """
            deal 2 cards to every one
            pp. 281
        :return:
        """
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # hide the dealers first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to other players
        for player in self.players:
            self.__aditional_cards(player)

        self.dealer.flip_first_card()  # reveal the dealers first card

        if not self.still_playing:
            # since all players have busted, show dealers hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__aditional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total():
                        player.lose()
                    else:
                        player.push()

        # remove all cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
