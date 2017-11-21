#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce
def checkio(number):
    l = []
    while(number):
        number, r = divmod(number, 10)
        if r:l.append(r)
    return reduce(lambda x,y: x*y, l)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
