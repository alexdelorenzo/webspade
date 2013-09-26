# -*- coding: utf-8 -*-
from Card import Card
import random


class Deck(object):
	def __init__(self):
		suits = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
		values = [x for x in range(2, 11)] + ['Queen', 'King', 'Jack', 'Ace']
		self.cards = [Card(v, s) for v in values for s in suits]

	def next_card(self):
		'''Returns card object'''
		return self.cards.pop()

	def return_to_stack(self, card, p='top'):
		'''Accepts card objects'''
		'''optionally can be put at the bottom of pile'''
		self.cards.append(card) if (p == 'top') else self.cards.insert(0, card)

	def shuffle(self, i=4):
		for x in range(i):
			random.shuffle(self.cards)