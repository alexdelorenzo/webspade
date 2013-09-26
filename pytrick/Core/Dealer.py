# -*- coding: utf-8 -*-
from Player import Player
class Dealer(Player):

    def __init__(self, num=0):
        super(Dealer, self).__init__()

    def deal(self, deck, player, number):
        for x in range(number):
            player.get_card(deck.next_card())

    def return_to_deck(self, deck, card, location='Bottom'):
        '''Accepts deck and card objects only'''
        deck.return_to_stack(card, location)

    def shuffle(self, deck):
        deck.shuffle()
