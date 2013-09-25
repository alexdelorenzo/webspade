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

    def selectCard(self):
        return int(input('Choose card index: '))

    def play(self, card):
        return self.giveCard(card)

    def lead(self, card):
        return self.giveCard(card)

    def lookAtHand(self, hand=None):
        if hand is None:
            hand = self.hand

