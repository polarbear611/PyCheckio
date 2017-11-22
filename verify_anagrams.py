#!/usr/bin/python
# -*- coding: utf-8 -*-

def lower_sorted(s):
    return sorted([c.lower() for c in ''.join(s.split(' '))])
def verify_anagrams(first_word, second_word):
    return lower_sorted(first_word) == lower_sorted(second_word)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"


