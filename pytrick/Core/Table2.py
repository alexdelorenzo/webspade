# -*- coding: utf-8 -*-
from Hand import Hand


class Table2(list):

    def __init__(self):
        super(Table2, self).__init__()
        self.groups = [Hand()]

    def newGroup(self):
        self.groups.append(Hand())

    def removeGroup(self, gIndex):
        return self.groups.pop(gIndex)

    def returnCardByIndex(self, gIndex, cIndex):
        return self.groups[gIndex].fromHand(self.groups[gIndex][cIndex])

    def addCardToGroup(self, cardObj, gIndex):
        self.groups[gIndex].toHand(cardObj)

    def joinGroups(self, gIndex1, gIndex2):
        for x in range(0, len(self.groups[gIndex2])):
            self.addCardToGroup(self.returnCardByIndex(x, gIndex2), gIndex1)
