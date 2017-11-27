#!/usr/bin/python
# -*- coding: utf-8 -*-

def p_nstep(p_sum, black, white):
    total = black + white
    return [[black * p_sum, black - 1 if black > 1 else 0, white + 1], [white * p_sum, black + 1, white - 1 if white > 1 else 0]]
def checkio(marbles, step):

    black = marbles.count('b')
    white = marbles.count('w')
    total = black + white
    state = {0:[[1, black, white]]}
    for i in range(1, step):
        si = []
        for s in state[i - 1]:
            si += p_nstep(*s)
        state[i] = si
    #第n次总
    sn = state[step - 1]
    print(sum([s[0] * s[2] for s in sn]) / pow(total, step)) 
    return round(sum([s[0] * s[2] for s in sn]) / pow(total, step), 2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
