# -*- coding: utf-8 -*-
from Core.Game import Game
from SpadesRules import SpadesRules, SpadesDealer
from PlayerActions import PlayerActions
import os


class Ledger(object):
	def __init__(self, players):
		self.players = {who: {'bid': 0, 'wins': 0, 'score': 0} for who in players}
		self.game = {'hand': -1, 'round': -1, 'trick_taker': -1}

	##
	## Properties can be get/set irrespective to the data structure
	##  overkill for now, but this class will be extracted and
	##  generalized later
	##

	@property
	def hand(self): return self.game['hand']
	@property
	def round(self): return self.game['round']
	@property
	def trick_taker(self): return self.game['trick_taker']

	@hand.setter
	def hand(self, val): self.game['hand'] = val
	@round.setter
	def round(self, val): self.game['round'] = val
	@trick_taker.setter
	def trick_taker(self, val): self.game['trick_taker'] = val



class Spades(Game):
	def __init__(self, players, cards):
		super(Spades, self).__init__()
		self.name = 'Spades'
		self.rules = SpadesRules()
		self.generate_deck()
		self.initiate_players(players)
		self.initiate_dealer()
		self.add_player(self.dealer)
		self.deal_cards(cards)
		self.initiate_table()
		self._assign_card_owners()

	@property
	def _card_in_play(self):
		card_sum = 0
		for who, plyr_obj in enumerate(self.players):
			card_sum += len(plyr_obj.hand)
			if len(plyr_obj.hand) > 0:
				return True
		if card_sum is 0:
			return False

	@property
	def _reached_500_yet(self):
		for who, plyr_obj in enumerate(self.players):
			if self.ledger.players[who]['score'] >= 500:
				return True
		return False

	@property
	def _highest_bidder(self):
		high_bidder, high_bid = 0, 0

		for who in range(len(self.players)):
			bid = self.ledger.players[who]['bid']
			high_bid = bid if bid > high_bid else high_bid
			high_bidder = who if bid is high_bid else high_bidder

		return high_bidder

	@property
	def next_player(self, override=False):
		'''Returns player index as integer'''

		first_hand = self.ledger.hand == 0
		no_trick_taker = self.ledger.trick_taker == -1

		first_turn_of_round = first_hand and no_trick_taker
		turn_after_card_played = self.ledger.hand >= 0
		turn_after_trick_taken = first_hand and not no_trick_taker
		last_card_played = self.ledger.hand == len(self.players)

		if override is True:
			return override
		elif first_turn_of_round is True:
			#print "DEBUG first_turn_of_round is True"
			#print "DEBUG self.highestBidder() is ", self.highestBidder()
			return self._highest_bidder
		elif turn_after_trick_taken is True:
			#print "DEBUG turn_after_trick_taken is True"
			return self.ledger.trick_taker
		elif turn_after_card_played is True:
			#print "DEBUG turn_after_card_played is True"
			owner_of_last_card = self.table.groups[0][-1].owner
			#print "DEBUG len(self.players) ", len(self.players)
			if owner_of_last_card + 1 is len(self.players):
				return 0
			else:
				return owner_of_last_card + 1
		elif last_card_played is True:
			#print "DEBUG last_card_played is True"
			return self.ledger.trick_taker
		else:
			raise Exception("Invalid turn")

	def _wins_to_score(self, win_set, diff_set):
		for who, plyr_dict in self.ledger.players.iteritems():
			if diff_set[who] < 0:
				plyr_dict['score'] -= diff_set[who]
			elif diff_set[who] is 0:
				plyr_dict['score'] += plyr_dict['bid'] * 10
			elif win_set[who] > 0:
				plyr_dict['score'] += plyr_dict['bid'] * 10 + diff_set[who]

	def _print_scores(self):
		for who, plyrObj in enumerate(self.players):
			print("Player ",  who,  "'s score: ", self.ledger.players[who]['score'])
			print("Player ",  who,  "'s tricks: ", self.ledger.players[who]['wins'])

	def _assign_card_owners(self):
		for who, plyrObj in enumerate(self.players):
			for card in range(0, len(self.players[who].hand)):
				self.players[who].hand[card].owner = who

	def _append_bids(self, player, bid):
		self.ledger.players[player]['bid'] = bid

	def _write_bids_to_ledger(self):
		for who, plyrObj in enumerate(self.players):
			self._append_bids(who, plyrObj.bids.pop())

	def _hand_counter(self):
		self.ledger.game['hand'] += 1

	def _play_card(self, player):
		self.table.add_card_to_group(
			self.players[player].play(
				self.players[player].selectCard()), 0)

	def _take_trick(self):
		trickTaker = self.rules.whoTakesTrick(self.table.groups[0])
		self.ledger.trick_taker = trickTaker
		print("Trick Taker: Player ", trickTaker)
		self.ledger.players[trickTaker]['wins'] += 1
		hand = self.table.remove_group(0)

		for card in range(len(hand)):
			self.deck.returnToStack(hand.pop())

	def initiate_players(self, intHumans):
		self.players = [PlayerActions(x) for x in range(0, intHumans)]

	def initiate_dealer(self):
		self.dealer = SpadesDealer()
		self.dealer.shuffle(self.deck)

	def generate_ledger(self):
		self.ledger = Ledger(range(len(self.players)))

	def initiate_bidding(self):
		for who, plyr_obj in enumerate(self.players):
			plyr_obj.bid(int(input('Player ' + str(who) + "'s bid: ")))
		self._write_bids_to_ledger()

	def new_game(self):
		self.generate_ledger()
		while self._reached_500_yet is False:
			self._print_scores()
			self.next_round()
			self._print_scores()
			self.dealCards(52 / len(self.players))
			self._assign_card_owners()

		if self._reached_500_yet is True:
			print("Motherfucking fuck the game is over.")
		self._print_scores()

	def next_round(self):
		self.ledger.game['round'] += 1
		os.system("clear")
		print("Round ", self.ledger.game['round'])

		self.initiate_bidding()

		card_in_play = True
		while card_in_play is True:
			self.next_hand()
			card_in_play = self._card_in_play

		bid_set, win_set, difference_set = [], [], []

		for who, plyr_obj in enumerate(self.players):
			bid_set.append(self.ledger.players[who]['bid'])
			win_set.append(self.ledger.players[who]['wins'])

		for who, plyr_obj in enumerate(self.players):
			difference_set.append((win_set[who] - bid_set[who]))

		self._wins_to_score(win_set, difference_set)


	def next_hand(self):
		self.ledger.hand += 1
		print("Hand ", self.ledger.game['hand'])

		for player in self.players:
			who = self.next_player()
			print("Player's Turn: ", who)
			self.players[who].lookAtHand()

			best = self.rules.highestCardInHand(self.players[who].hand)
			playable = self.rules.playableCardsInHand(self.table.groups[0], self.players[who].hand)
			print("\nBest card in hand: ", best)
			print("Playable cards in hand: ", playable)

			print("Cards on table: ", self.players[who].lookAtHand(self.table.groups[0]), "\n")

			self._play_card(who)
			self._hand_counter()

		self._take_trick()
		self.ledger.hand = -1
		self.table.newGroup()

