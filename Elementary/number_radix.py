#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(str_number, radix):
    result = 0
    for i, n in enumerate(reversed(str_number)):
        if n.isalpha():
            n = ord(n) - ord('A') + 10
        if int(n) >= radix:
            return -1
        result += int(n) * pow(radix, i) 
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
