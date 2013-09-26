# -*- coding: utf-8 -*-
from Hand import Hand

class Player(object):
    def __init__(self, num=0, handle='none'):
        self.hand = Hand()
        self.id = num
        self.hanlde = handle
        self.score = ''

    def pick_up_card(self, deck, num=1):
        '''Accepts deck object, optionally choose num of iterations'''
        for x in range(num):
            self.hand.to_hand(deck.next_card())

    def get_card(self, card):
        '''Accepts card objects only'''
        self.hand.to_hand(card)

    def give_card(self, card):
        return self.hand.from_hand(card)

    def place_card(self, card, hand):
        hand.to_hand(self.give_card(card))

    def flip_card(self, card):
        card.flip()

    def look_at_card(self, index, hand=None):
        if hand is None:
            hand = self.hand

        print(hand[index].color() +" "+ str(hand[index].value) +" of "+
             hand[index].suit)

    def look_at_hand(self, hand=None):
        if hand is None:
            hand = self.hand

        print(str(len(hand)) + " card(s) in hand.\n")
        for x in range(0, len(hand)):
            self.look_at_card(x, hand)

