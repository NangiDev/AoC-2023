from aoc import get_input, get_test_input
import re

DAY = 4
PART = "b"


if __name__ == "__main__":
    data = get_test_input(PART, DAY).splitlines()
    data = get_input(DAY).splitlines()

    total = 0
    cards = {}

    for idx, line in enumerate(data):
        (win, lot) = line[7:].split('|')
        win = win.strip().replace("  ", ' ').split(' ')
        lot = lot.strip().replace("  ", ' ').split(' ')
        match = set(win) & set(lot)
        
        #card = (idx, win, lot, len(match))
        card = (idx, len(match))
        cards[idx] = [card]


    tmp_c = cards.copy()
    for idx, card in enumerate(tmp_c):
        roof= tmp_c[card][0][1]
        for i in range(1,roof+1):
            cards[card + i].extend(cards[card])


    # for idx, card in enumerate(cards):
    #     print(card, len(cards[card]))
        
    # 1 2 4 8 14 1
    # 30

    for card in cards:
        total += len(cards[card])

    print(total)


