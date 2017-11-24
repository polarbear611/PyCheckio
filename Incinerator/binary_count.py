#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(number):
    l = []
    while(number):
        number, r = divmod(number, 2)
        l.append(r)
    return l.count(1)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9

