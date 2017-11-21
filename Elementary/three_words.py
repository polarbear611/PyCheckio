#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(words):
    words = words.split(' ')
    count_w = 0
    for i in range(len(words)):
        if all(c.isalpha() for c in words[i]):
            count_w += 1
            if count_w >=3:
                return True
        else:
            count_w = 0
                    
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
