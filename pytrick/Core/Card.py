# -*- coding: utf-8 -*-

class Card(list):
    def __init__(self, value, suit):
        self.is_orig_value = True
        self.value = value
        self.suit = suit
        self.modified_value = self.value
        self.face = 'Down'
        self.owner = 0

        self.append(self.true_value())
        self.append(str(suit))


    def color(self):
        return 'Red' if (self.suit == 'Diamonds' or self.suit == 'Hearts') else 'Black'

    def flip(self):
        self.face = 'Down' if (self.face == 'Up') else 'Up'

    def true_value(self):
        if self.is_orig_value is True:
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
            return self.modified_value

    def new_value(self, value):
        self.modified_value = value
        self.is_orig_value = False