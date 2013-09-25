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
        self.replaceTrump('Spades')

    def returnSuit(self, handObj):
        if len(handObj) is not 0:
            return handObj[-1].suit
        else:
            return None

    def followsSuit(self, handObj, cardObj):
        if self.returnSuit(handObj) == cardObj.suit:
            return True
        elif self.returnSuit(handObj) is None:
            return True
        else:
            return False

    def highestCardInHand(self, handObj):
        unsortedHand = copy.deepcopy(handObj)
        for card in unsortedHand:
            card.append(unsortedHand.index(card))

        sortedHand = sorted(unsortedHand, key=lambda x: x[0], reverse=True)
        return [sortedHand[card][2] for card in range(len(sortedHand))][0:4]

    def searchTrump(self, handObj, returnCardObj=False):
        if self.isTrumpInHand(handObj) is True:
            trumps = []
            for x in range(0, len(handObj)):
                for y in range(0, len(self.trump)):
                    if handObj[x].suit is self.trump[y]:
                            trumps.append(x)

            return [handObj[index] for index in trumps]
        else:
            return False

    def highestTrumpInHand(self, handObj):
        handCopy = copy.deepcopy(handObj)
        if self.searchTrump(handCopy) is not False:
            highIndex, lastTrump, trumps = 0, 0, []
            for trump in self.searchTrump(handCopy):
                 trumps.append(trump)
            return self.highestCardInHand(self.searchTrump(handObj))
        else:
            return False

        #for x in range(0, len(self.trump))
    def isCardPlayable(self, tHandObj, cardObj):
        for x in range(0, len(self.trump)):
            if cardObj.suit is self.trump[x]:
                return True
                break
            elif self.followsSuit(tHandObj, cardObj) is True:
                return True
                break
            elif x is len(self.trump) - 1:
                return False
                break

    def playableCardsInHand(self, tHandObj, handObj):
        cards = Hand()
        for cardIndex in range(0, len(handObj)):
            if self.isCardPlayable(tHandObj, handObj[cardIndex]) is True:
                cards.append(cardIndex)
        if len(cards) is len(handObj):
            return "Any, it's your lead!"
        elif len(cards) > 0:
            return cards
        elif len(cards) is 0:
            return False


    def whoTakesTrick(self, handObj):
        if self.highestTrumpInHand(handObj) is not False:
            print("DEBUG Trump in hand.")
            indexOfTrump = self.highestTrumpInHand(handObj)
            print(indexOfTrump)
            print(int(handObj[indexOfTrump[0]].owner))
            return int(handObj[indexOfTrump[0]].owner)
        else:
            #print("DEBUG Finding highest value card")
            sortedHand = sorted(handObj, key=lambda x: x[0], reverse=True)
            return int(sortedHand[0].owner)
