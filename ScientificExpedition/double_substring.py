#!/usr/bin/python
# -*- coding: utf-8 -*-

def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    # your code here
    max_length = 0
    sub_length = 1
    line_length = len(line)
    while(sub_length <= line_length // 2):
        for i in range(line_length - sub_length):
           if line[i + sub_length:].find(line[i : i + sub_length]) >= 0:
                max_length = sub_length
                break
        sub_length += 1
    return max_length

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')

