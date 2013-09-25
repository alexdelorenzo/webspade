# -*- coding: utf-8 -*-

class Card(list):
    def __init__(self, value, suit):
        self.blnOrigValue = True
        self.value = value
        self.suit = suit
        self.modifiedvalue = self.value
        self.face = 'Down'
        self.owner = 0

        self.append(self.trueValue())
        self.append(str(suit))


    def color(self):
        return 'Red' if (self.suit == 'Diamonds' or self.suit == 'Hearts') else 'Black'

    def flip(self):
        self.face = 'Down' if (self.face == 'Up') else 'Up'

    def trueValue(self):
        if self.blnOrigValue is True:
            if (2 <= self.value <= 10):
                return int(self.value)
            elif self.value == 'Jack':
                return 11
            elif self.value == 'Queen':
                return 12
            elif self.value == 'King':
                return 13
            elif self.value == 'Ace':
                return 1
        else:
            return self.modifiedvalue

    def newValue(self, value):
        self.modifiedvalue = value
        self.blnOrigValue = False