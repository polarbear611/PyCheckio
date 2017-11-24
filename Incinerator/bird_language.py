#!/usr/bin/python
# -*- coding: utf-8 -*-

VOWELS = "aeiouy"
def translate(phrase):
    ps = phrase.split(' ')
    words = []
    for p in ps:
        word = ''
        i = 0
        while i < (len(p)):
            if p[i] in VOWELS:
                word += p[i]
                i += 3
            else:
                word += p[i]
                i += 2
        words.append(word) 
    return ' '.join(words)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

