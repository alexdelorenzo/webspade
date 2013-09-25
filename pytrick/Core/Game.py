# -*- coding: utf-8 -*-
from Deck import Deck
from Player import Player
from Dealer import Dealer
from Hand import Hand
from Table2 import Table2

class Game(object):

    def __init__(self):
        return

    def generateDeck(self):
        self.deck = Deck()

    def initiatePlayers(self, intHumans=2, intAI=0):
        self.players = [Player(str(x)) for x in range(intHumans)]

    def initiateDealer(self):
        self.dealer = Dealer()
        self.dealer.shuffle(self.deck)

    def initiateTable(self):
        self.table = Table2()

    def addPlayer(self, player):
        '''Accepts the player object'''
        self.players.append(player)

    def dealCards(self, numberOfCards=0):
        for x in range(len(self.players)):
            self.dealer.deal(self.deck, self.players[x], numberOfCards)
    def debug(self):
        self.dealer.deal(self.deck, self.players[1], 12)
        self.dealer.deal(self.deck, self.players[0], 12)
        print(self.players[1].hand[1])
        self.players[1].lookAtHand()
        print('    Create table object')
        t = Table2()


        for x in range(0, len(self.players[1].hand)):
            print('    ' + `x` + " of " + `len(self.players[1].hand)`)
            print(`self.players[1].hand[x].value` + " of " + self.players[1].hand[x].suit +
                    " owned by " + `self.players[1].hand[x].owner`)
        print('    Groups printout')
        print(t.groups)
        print('    Group printout')
        print(t.groups[0])
        print('\n\n\n    Add New Group')
        t.newGroup()
        print('    Groups printout')
        print(t.groups)
        print('    Group printout')
        print(t.groups[1])
        print('\n\n\n    Add card from hand to group[0]')
        t.addCardToGroup(self.players[1].giveCard(1), 0)
        print('    Groups printout')
        print(t.groups)
        print('    Group printout')
        print(t.groups[1])
        print('\n\n\n    Add Three cards to group[1]')
        t.addCardToGroup(self.players[1].giveCard(3), 1)
        t.addCardToGroup(self.players[1].giveCard(2), 1)
        t.addCardToGroup(self.players[1].giveCard(0), 1)
        print('    Groups printout')
        print(t.groups)
        print('    Group printout')
        print(t.groups[1])

def main():
    g = Game()
    g.generateDeck()
    g.initiateDealer()
    g.initiatePlayers(2)
    g.addPlayer(g.dealer)


if __name__ == '__main__':
    main()