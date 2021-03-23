import numpy as np
deck = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

bt = []
for i in range(len(deck)-1,-1,-1):
    t = []
    for j in range(len(deck)-1,-1,-1):
        if i == j:
            t.append(deck[i] + deck[j])
        elif j < i:
            t.append(deck[max(i,j)] + deck[min(i,j)] + "s")
        else:
            t.append(deck[max(i,j)] + deck[min(i,j)] + "o")
    bt.append(t)


cover = np.array(bt)
print(cover.shape)

