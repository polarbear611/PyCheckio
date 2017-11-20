#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(text):

    #replace this for solution
    d = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
    return sorted([k for k,v in d.items() if v == max(d.values())])[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

