# -*- coding: utf-8 -*-
from Game import Game

class TrickGames(Game):

    def __init__(self):
        super(TrickGames, self).__init__()
        self.trump = ['']
        self.bln_trump = False

    def replace_trump(self, trump, index=0):
        self.trump[index] = trump

    def add_trump(self, trump):
        self.trump.append(trump)

    def del_trump(self, trump):
        self.trump.pop(self.trump.index(trump))

    def is_trump_in_hand(self, hand_obj):
        in_hand = False
        for x in range(0, len(hand_obj)):
            for y in range(0, len(self.trump)):
                if hand_obj[x].suit is self.trump[y]:
                    in_hand = True
        return in_hand

    def can_lead_with(self, card):
        if self.bln_trump is True:
            return

    def trump_played(self):
        if self.bln_trump is True:
            return