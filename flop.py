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
    flop = []
    flop_card = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    flpo_suit = [0,0,0,0]

    def __init__(self, text):
        self.set_flop(text)

    def set_flop(self, text):
        if ' ' in text:
            temp = text.split(' ')
        else:
            temp = [text[0:2], text[2:4], text[4:6]]
        self.flop = temp.copy()

    def card_and_suit_count(self):
        for card in self.flop

    def get_flop_card(self):
        return self.flop_card

    def __str__(self):
        return self.flop[0] + self.flop[1] + self.flop[2]


if __name__ == '__main__':
    t = Flop('AcTc5d')
    print(t)
