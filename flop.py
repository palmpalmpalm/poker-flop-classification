from range import Range
import numpy as np


class Flop:
    flop_card = []

    def __init__(self, text):
        self.set_flop(text)

    def set_flop(self, text):
        if ' ' in text:
            temp = text.split(' ')
        else:
            temp = [text[0:2], text[2:4], text[4:6]]
        self.flop_card = temp.copy()

    def get_flop_card(self):
        return self.flop_card

    def __str__(self):
        return self.flop_card[0] + self.flop_card[1] + self.flop_card[2]


if __name__ == '__main__':
    t = Flop('AcTc5d')
    print(t)
