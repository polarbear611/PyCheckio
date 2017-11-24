#!/usr/bin/python
# -*- coding: utf-8 -*-

def palindromic(text):
    return text == text[::-1]
    
def longest_palindromic(text):
    if len(text) == 1:
        return text
    result = ""
    for i in range(len(text) - 1):
        for j in range(i+1, len(text) + 1):
            if palindromic(text[i:j]) and len(text[i:j]) > len(result):
                result = text[i:j]
    print (result)
    return result

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

