#!/usr/bin/python
# -*- coding: utf-8 -*-

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    words = text.replace(',', ' ').replace('.', ' ').strip().upper().split(' ')
    count = 0
    for w in words:
        if len(w) > 1 and not any(i.isdigit() for i in w) and \
        all( not (w[i] in VOWELS and w[i+1] in VOWELS) for i in range(len(w) - 1)) and \
        all(not (w[i] in CONSONANTS and w[i+1] in CONSONANTS) for i in range(len(w) - 1) ):
            count += 1
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

