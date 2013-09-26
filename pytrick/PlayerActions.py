# -*- coding: utf-8 -*-
from Core.Player import Player

class PlayerActions(Player):

    def __init__(self, num=0):
        super(PlayerActions, self).__init__(num=0)
        self.bids = []
        self.id = num
        self.turn = False

    def bid(self, tricks):
        self.bids.append(tricks)

    def select_card(self):
        return int(input('Choose card index: '))

    def play(self, card):
        return self.give_card(card)

    def lead(self, card):
        return self.give_card(card)

    def look_at_hand(self, hand=None):
        if hand is None:
            hand = self.hand

