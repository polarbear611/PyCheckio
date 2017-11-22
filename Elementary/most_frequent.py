#!/usr/bin/python
# -*- coding: utf-8 -*-

def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    from collections import Counter
    c = Counter(data)
    return c.most_common(1)[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
