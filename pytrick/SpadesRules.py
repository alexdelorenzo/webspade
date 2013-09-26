# -*- coding: utf-8 -*-
from Core.TrickGames import TrickGames
from Core.Dealer import Dealer
from Core.Hand import Hand
from PlayerActions import PlayerActions
import copy


class SpadesDealer(Dealer, PlayerActions):

    def __init__(self):
        super(SpadesDealer, self).__init__()


class SpadesRules(TrickGames):

    def __init__(self):
        super(SpadesRules, self).__init__()
        self.replace_trump('Spades')

    @staticmethod
    def return_suit(hand_obj):
        if len(hand_obj) is not 0:
            return hand_obj[-1].suit
        else:
            return None

    def follows_suit(self, hand_obj, card_obj):
        if self.return_suit(hand_obj) == card_obj.suit:
            return True
        elif self.return_suit(hand_obj) is None:
            return True
        else:
            return False

    def highest_card_in_hand(self, hand_obj):
        unsorted_hand = copy.deepcopy(hand_obj)
        for card in unsorted_hand:
            card.append(unsorted_hand.index(card))

        sorted_hand = sorted(unsorted_hand, key=lambda x: x[0], reverse=True)
        return [sorted_hand[card][2] for card in range(len(sorted_hand))][0:4]

    def search_trump(self, hand_obj, return_card_obj=False):
        if self.is_trump_in_hand(hand_obj) is True:
            trumps = []
            for x in range(0, len(hand_obj)):
                for y in range(0, len(self.trump)):
                    if hand_obj[x].suit is self.trump[y]:
                            trumps.append(x)

            return [hand_obj[index] for index in trumps]
        else:
            return False

    def highest_trump_in_hand(self, hand_obj):
        hand_copy = copy.deepcopy(hand_obj)
        if self.search_trump(hand_copy) is not False:
            high_index, last_trump, trumps = 0, 0, []
            for trump in self.search_trump(hand_copy):
                 trumps.append(trump)
            return self.highest_card_in_hand(self.search_trump(hand_obj))
        else:
            return False

        #for x in range(0, len(self.trump))
    def is_card_playable(self, table_hand_obj, card_obj):
        for x in range(0, len(self.trump)):
            if card_obj.suit is self.trump[x]:
                return True
                break
            elif self.follows_suit(table_hand_obj, card_obj) is True:
                return True
                break
            elif x is len(self.trump) - 1:
                return False
                break

    def playable_cards_in_hand(self, tbl_hand_obj, hand_obj):
        cards = Hand()
        for card_index in range(0, len(hand_obj)):
            if self.is_card_playable(tbl_hand_obj, hand_obj[card_index]) is True:
                cards.append(card_index)
        if len(cards) is len(hand_obj):
            return "Any, it's your lead!"
        elif len(cards) > 0:
            return cards
        elif len(cards) is 0:
            return False


    def who_takes_trick(self, hand_obj):
        if self.highest_trump_in_hand(hand_obj) is not False:
            print("DEBUG Trump in hand.")
            index_of_trump = self.highest_trump_in_hand(hand_obj)
            print(index_of_trump)
            print(int(hand_obj[index_of_trump[0]].owner))
            return int(hand_obj[index_of_trump[0]].owner)
        else:
            #print("DEBUG Finding highest value card")
            sorted_hand = sorted(hand_obj, key=lambda x: x[0], reverse=True)
            return int(sorted_hand[0].owner)
