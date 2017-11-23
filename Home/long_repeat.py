#!/usr/bin/python
# -*- coding: utf-8 -*-

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if not line:
        return 0
    max_l = max_c = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            max_c += 1
            max_l = max(max_c, max_l)
        else:
            max_c = 1
    return max_l

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

