# -*- coding: utf-8 -*-
from Card import Card
import random

SUITS = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
VALUES = [x for x in range(2, 11)] + ['Queen', 'King', 'Jack', 'Ace']


class Deck(object):
    def __init__(self):
        self.cards = [Card(v, s) for v in VALUES for s in SUITS]
        print "DEBUG ", self.cards[0].value

    def nextCard(self):
        '''Returns card object'''
        return self.cards.pop()

    def returnToStack(self, card, p='top'):
        '''Accepts card objects'''
        '''optionally can be put at the bottom of pile'''
        self.cards.append(card) if (p == 'top') else self.cards.insert(0, card)

    def shuffle(self, i=4):
        for x in range(i):
            random.shuffle(self.cards)

