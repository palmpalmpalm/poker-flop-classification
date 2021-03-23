import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

deck2 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
deck = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

# init cover
cover_list_temp = []
for i in range(len(deck2) - 1, -1, -1):
    cover_row_temp = []
    for j in range(len(deck2) - 1, -1, -1):
        if i == j:
            cover_row_temp.append(deck2[i] + deck2[j])
        elif j < i:
            cover_row_temp.append(deck2[max(i, j)] + deck2[min(i, j)] + "s")
        else:
            cover_row_temp.append(deck2[max(i, j)] + deck2[min(i, j)] + "o")
    cover_list_temp.append(cover_row_temp)

cover = np.array(cover_list_temp)


# return position of combo in 13x13 table as i,j
def get_combo_position(combo):
    n = len(combo)
    first_card = combo[0]
    second_card = combo[1]
    index_first_card = deck.index(first_card)
    index_second_card = deck.index(second_card)

    if n == 2:  # it's pocket
        return index_first_card, index_second_card
    elif n == 3:
        if combo[2] == 's':  # it's suit
            return index_first_card, index_second_card
        else:  # if not suit then it's off suit
            return index_second_card, index_first_card


# return combo of this position i,j
def pos_to_combo(i, j):
    if i == j:  # pocket
        return deck[i] + deck[j]
    elif j < i:  # suit
        return deck[i] + deck[j] + 's'
    else:  # off suit
        return deck[i] + deck[j] + 'o'


class Range:
    # init range to 0 combos
    len_deck = len(deck)
    range_c = np.zeros((len_deck, len_deck))
    range_p = np.zeros((len_deck, len_deck))

    def __init__(self, text='None'):
        if text == 'None':
            return
        self.set_range(text)

    def set_range(self, text):
        text_order = text.split(',')
        # print(text_order)
        weight = 100.0
        for order in text_order:
            if order[0] == '[':
                weight = float(order[1:5])

            start_index = order.find(']')
            if start_index == -1:
                start_index = 0
            else:
                start_index += 1  # shift 1

            stop_index = order.find('[', start_index)
            if stop_index == -1:
                stop_index = len(order)

            if '/' in order:
                if order[0] != '[':
                    stop_index = order.find('[')
                    start_index = 0

            if '-' in order:
                start_combo, stop_combo = order[start_index:stop_index].split('-')
                i, j = get_combo_position(start_combo)
                ie, je = get_combo_position(stop_combo)
                while i != ie or j != je:
                    self.add_combo(i, j, weight)
                    if i == j:  # pocket
                        i += 1
                        j += 1
                    elif j < i:  # suit
                        i += 1
                    else:  # off suit
                        j += 1
                self.add_combo(ie, je, weight)
            else:
                i, j = get_combo_position(order[start_index:stop_index])
                self.add_combo(i, j, weight)

            if order[len(order) - 1] == ']':
                weight = 100.0

        self.set_percent_range()

    def set_percent_range(self):
        for i in range(self.len_deck):
            for j in range(self.len_deck):
                if i == j:  # pocket
                    self.range_p[i, j] = (self.range_c[i, j] / 6) * 100
                elif j < i:  # suit
                    self.range_p[i, j] = (self.range_c[i, j] / 4) * 100
                else:  # off suit
                    self.range_p[i, j] = (self.range_c[i, j] / 12) * 100

    # add combo to range
    def add_combo(self, i, j, weight=100):
        if i == j:  # pocket
            w = (weight / 100) * 6
            self.range_c[i, j] = w
        elif j < i:  # suit
            w = (weight / 100) * 4
            self.range_c[i, j] = w
        else:  # off suit
            w = (weight / 100) * 12
            self.range_c[i, j] = w

    # fill range to 100%
    def fill_100_range(self):
        for i in range(self.len_deck):
            for j in range(self.len_deck):
                if i == j:
                    self.range_c[i, j] = 6
                elif j < i:
                    self.range_c[i, j] = 4  # suit combo
                else:
                    self.range_c[i, j] = 12  # off suit

    # get percent of available combos in range
    def get_percent_of_range(self):
        total_combos = np.sum(self.range_c)
        return (total_combos / 1326) * 100

    # get number of input combo
    def get_combo(self, combo):
        i, j = get_combo_position(combo)
        return self.range_c[i, j]

    # set number of input combo
    def set_combo(self, number, combo):
        i, j = get_combo_position(combo)
        self.range_c[i, j] = number

    # get number of input combo by position
    def get_combo_by_pos(self, i, j):
        return self.range_c[i, j]

    # set number of input combo by position
    def set_combo_by_pos(self, number, i, j):
        self.range_c[i, j] = number

    # display number of combos in range
    def show_combos(self):
        fig, ax = plt.subplots()
        ax = sns.heatmap(self.range_c, annot=self.range_c, square=True, color='white')
        ax.set_title('Range')
        ax.xaxis.tick_top()
        ax.set_xticklabels(deck)
        ax.set_yticklabels(deck, rotation=0)
        plt.tight_layout()
        plt.show()

    # display percent of combos in range
    def show_range(self):
        fig, ax = plt.subplots()
        ax = sns.heatmap(self.range_p, annot=cover, fmt='', cmap="YlGnBu", linewidths=.5, linecolor='black',
                         square=True)
        ax.set_title('Range')
        ax.xaxis.tick_top()
        ax.set_xticklabels(deck)
        ax.set_yticklabels(deck, rotation=0)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    t = input("Enter range : ").strip()
    A = Range(t)
    A.show_combos()
    A.show_range()
    # print(get_combo_position('AQs'))
    # B = Range()
    # B.add_combo('AKs',100)
    # B.show_combos()

    # C = Range('AA,[50.0]KK[/50.0]')
    # C.show_combos()

    # D = Range('AKo-AJo')
    # D.show_combos()