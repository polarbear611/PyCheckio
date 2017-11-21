#!/usr/bin/python
# -*- coding: utf-8 -*-

def say_hi(name, age):
    """
        Hi!
    """
    # your code here
    return "Hi. My name is {} and I'm {} years old".format(name, age)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
