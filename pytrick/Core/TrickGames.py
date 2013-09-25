# -*- coding: utf-8 -*-
from Game import Game

class TrickGames(Game):

    def __init__(self):
        super(TrickGames, self).__init__()
        self.trump = ['']
        print(self.trump[0])
        self.blnTrump = False

    def replaceTrump(self, trump, index=0):
        self.trump[index] = trump

    def addTrump(self, trump):
        self.trump.append(trump)

    def delTrump(self, trump):
        self.trump.pop(self.trump.index(trump))

    def isTrumpInHand(self, handObj):
        inHand = False
        for x in range(0, len(handObj)):
            for y in range(0, len(self.trump)):
                if handObj[x].suit is self.trump[y]:
                    inHand = True
        return inHand
    def canLeadWith(self, card):
        if self.blnTrump is True:
            return

    def trumpPlayed(self):
        if self.blnTrump is True:
            return