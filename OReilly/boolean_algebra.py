#!/usr/bin/python
# -*- coding: utf-8 -*-

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if OPERATION_NAMES[0] == operation:
        return int(x and y)
    if OPERATION_NAMES[1] == operation:
        return int(x or y)
    if OPERATION_NAMES[2] == operation:
        return int(not x or y)
    if OPERATION_NAMES[3] == operation:
        return int((x or y) and not (x and y))
    if OPERATION_NAMES[4] == operation:
        return int(x == y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

