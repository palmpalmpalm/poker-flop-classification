from range import Range
import numpy as np

deck = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
deck2 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suit = ['c', 'd', 'h', 's']

A = ['A']
HIGH = ['T', 'J', 'Q', 'K']
MED = ['6', '7', '8', '9']
LOW = ['2', '3', '4', '5']
group = [[A, 'A'], [HIGH, "H"], [MED, "M"], [LOW, "L"]]

FH = ["TRIPS", "PAIRED", "UNPAIRED"]  # Full Houses Type
FL = ["RAINBOW", "TWO-TONE", "MONOTONE"]  # Flushes Type
STR = ["OESD", "GUTSHOT", "STRAIGHT", "NONE"]  # Straights Type


class Flop:
    # create list of flop, card in flop, and suit in flop
    flop = []
    flop_card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    flop_suit = [0, 0, 0, 0]

    # init flop with input flop
    def __init__(self, text):
        self.set_flop(text)

    # set flop
    @classmethod
    def set_flop(cls, text):
        if ' ' in text:
            temp = text.split(' ')
        else:
            temp = [text[0:2], text[2:4], text[4:6]]
        cls.flop = temp.copy()
        cls.card_and_suit_count()

    # count card and suit
    @classmethod
    def card_and_suit_count(cls):
        for card in cls.flop:
            temp_card = card[0]
            temp_suit = card[1]
            cls.flop_card[deck.index(temp_card)] += 1
            cls.flop_suit[suit.index(temp_suit)] += 1
        print(cls.flop_card, cls.flop_suit)

    # return flop
    @classmethod
    def get_flop_card(cls):
        return cls.flop

    # print flop
    def __str__(self):
        return self.flop[0] + self.flop[1] + self.flop[2]


if __name__ == '__main__':
    t = Flop('AcTc5d')
    print(t)
