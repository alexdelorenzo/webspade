from pytrick.Spades import Spades
from collections import defaultdict, deque

USER_MIN = 0
USER_MAX = 0
CARDS = 52


class WebInterface(dict):
  def __init__(self):
    self.rules = defaultdict(dict)
    self.rules['users']['min'], self.rules['users']['max'] = USER_MIN, USER_MAX
    
  def initiate_users(self, num):
    min, max = self.limits['users']['min'], self.limits['users']['max']
    if min < num < max:
      self.game_instance(num, CARDS / num)

  def post_chosen_card(self, cardIndex, player):
    self.unprocessed_turn = (cardIndex, player)

  def get_chosen_card(self):
      chosen_tuple = self.unprocessed_turn
      self.unprocessed_turn = False
      return chosen_tuple

  def post_bids(self, plyr_bids=dict()):
    if plyr_bids: pass
      #self.plyr_bids = plyr_bids
    else:
      raise ValueError('fuckFucjkfUFUCKFUCKL')

  def choose_card(self, player):
    pass

  def return_bid(self, player):
    pass


class SpadesWeb(Spades):
  def __init__(self, players):
    super(SpadesWeb, self).__init__(players - 1, self._cards_by_users(players))

  def _cards_by_users(self, players):
    cards_in_deck = 52
    return 52 / players

  def _play_card(self, player, card):
    #card, player = self.web.get_chosen_card()

    self.table.addCardToGroup(
    self.players[player].play(card), 0)

  def initiate_bidding(self):
    """Misleading name, it submits bids like a bitch"""
    for who, bid in self.web.plyr_bids.iteritems():
      self.players[who].bid(bid)
    self._write_bids_to_ledger()



