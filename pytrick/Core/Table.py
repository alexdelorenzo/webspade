# -*- coding: utf-8 -*-
from Hand import Hand

class Table(list):
    def __init__(self):
        super(Table, self).__init__()
        self.groups = [Hand(), Hand()]
        print("-----Initiate Table, group matrix below:")
        print(self.groups)
        self.indice = []


    def createGroup(self, card1=[], card2=[]):
        if len(card2) is 0:
            self.groups.append(Hand(card1))
        else:
            newgroup = len(self.groups)
            self.groups[newgroup].append(card1)
            self.groups[newgroup].append(card2)

    def lookAtGroups(self):
        self.indice = [[[x, y], [self.groups[x][y].trueValue(), self.groups[x][y].suit]] for
            x in range(0, len(self.groups))
            for y in range(0, (len(self.groups[x])))]
        return self.indice

    def placeCard(self, card, sub1):
        bln = False
        for x in range(0, len(self.groups) - 1):
            print('-----Find card in pile and pop it, length of self.groups: ' + (str(len(self.groups))))
            try:
                self.groups[x].find(card)
                print('Found card')
                self.groups[sub1].append(self.groups[x].pop(card))
                print('Swappped Duplicate')
                bln = True
                break
            except:
                print("-----ERROR")
        if bln is False:
            print("-----" + str(card.trueValue()) + card.suit + " added to group " +
                    str(sub1))
            self.groups[sub1].append(card)

    def pickUpCard(self, sub1, sub2):
        '''Returns card object'''
        return self.groups[sub1]
