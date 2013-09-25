# -*- coding: utf-8 -*-

class Hand(list):

    def __init__(self, card=[]):
        super(Hand, self).__init__()
        self.owner = int(0)
        if len(card) is 0:
            return
        else:
            self.toHand(card)

    def toHand(self, card):
        self.append(card)

    def fromHand(self, index):
        return self.pop(index)

    def isInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def find(self, card):
        if self.isInt(self.index(card)) is False:
            print('ook')
            print("-----" + str(card) + " is not found!")
        else:
            print("----- Found Card: " + self.index(card))
            return self.pop(self.index(card))
