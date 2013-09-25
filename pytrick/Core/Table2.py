# -*- coding: utf-8 -*-
from Hand import Hand


class Table2(list):

    def __init__(self):
        super(Table2, self).__init__()
        self.groups = [Hand()]

    def new_group(self):
        self.groups.append(Hand())

    def remove_group(self, g_index):
        return self.groups.pop(g_index)

    def return_card_by_index(self, gIndex, cIndex):
        return self.groups[gIndex].fromHand(self.groups[gIndex][cIndex])

    def add_card_to_group(self, card_obj, g_index):
        self.groups[g_index].toHand(card_obj)

    def join_groups(self, g_index1, g_index2):
        for x in range(0, len(self.groups[g_index2])):
            self.add_card_to_group(
	            self.return_card_by_index(x, g_index2),
	            g_index1)
