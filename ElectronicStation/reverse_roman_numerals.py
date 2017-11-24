#!/usr/bin/python
# -*- coding: utf-8 -*-

def reverse_roman(roman_string):
    #replace this for solution
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']
    val = 0
    for t in thousands[::-1]:
        if t and roman_string.find(t) >= 0:
            val += 1000 * thousands.index(t)
            break
    for t in hundreds[::-1]:
        if t and roman_string.find(t) >= 0:
            if t == 'D':
                if roman_string.find('CD') >= 0:val += 400
                else:val += 500
                break;
            if t == 'C' and roman_string.find('XC') >= 0:
                break
            val += 100 * hundreds.index(t)
            break
    for t in tens[::-1]:
        if t and roman_string.find(t) >= 0:
            if t == 'L':
                if roman_string.find('XL') >= 0:val += 40
                else:val += 50
                break;
            else:
                val += 10 * tens.index(t)
                break
    for t in ones[::-1]:
        if t and roman_string.find(t) >= 0:
            if t == 'V':
                if roman_string.find('IV') >= 0:val += 4
                else:val += 5
                break;
            else:
                val += ones.index(t)
                break
    print(val)
    return val

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
