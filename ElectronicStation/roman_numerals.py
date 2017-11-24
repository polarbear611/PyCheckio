#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce

def checkio(data):
    #replace this for solution
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
    thousands = ['', 'M', 'MM', 'MMM']
    thou, data = divmod(data, 1000)
    hun, data = divmod(data, 100)
    ten, one = divmod(data, 10)
    
    return thousands[thou] + hundreds[hun] + tens[ten] + ones[one]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
