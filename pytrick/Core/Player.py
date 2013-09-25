# -*- coding: utf-8 -*-
from Hand import Hand

class Player(object):
    def __init__(self, num=0, handle='none'):
        self.hand = Hand()
        self.id = num
        self.hanlde = handle
        self.score = ''

    def pickUpCard(self, deck, num=1):
        '''Accepts deck object, optionally choose num of iterations'''
        for x in range(num):
            self.hand.toHand(deck.nextCard())

    def getCard(self, card):
        '''Accepts card objects only'''
        self.hand.toHand(card)

    def giveCard(self, card):
        return self.hand.fromHand(card)

    def placeCard(self, card, hand):
        hand.toHand(self.giveCard(card))

    def flipCard(self, card):
        card.flip()

    def lookAtCard(self, index, hand=None):
        if hand is None:
            hand = self.hand

        print(hand[index].color() +" "+ str(hand[index].value) +" of "+
             hand[index].suit)

    def lookAtHand(self, hand=None):
        if hand is None:
            hand = self.hand

        print(str(len(hand)) + " card(s) in hand.\n")
        for x in range(0, len(hand)):
            self.lookAtCard(x, hand)

