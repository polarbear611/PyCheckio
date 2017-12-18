#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(data):
    """The sum of two integer elements"""
    a, b = data
    return data[0] + data[1]
    
if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'

