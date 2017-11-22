#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(first, second):
    return ','.join(sorted(list(set([f for f in first.split(',') for s in second.split(',') if f==s]))))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

