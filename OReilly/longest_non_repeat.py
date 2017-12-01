#!/usr/bin/python
# -*- coding: utf-8 -*-

def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    # your code here
    try:
        longest = line[0]
        for i in range(len(line)):
            nr_str = line[i]
            for j in range(i+1, len(line)):
                if line[j] not in nr_str:
                    nr_str += line[j]
                else:
                    break
            if len(nr_str) > len(longest):
                longest = nr_str
        return longest
    except IndexError:
        return ''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')

