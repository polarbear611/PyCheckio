#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_cookie(cookie, name):
    d = {}
    for c in cookie.split('; '):
        i,v = c.split('=')
        d[i] = v
    return d[name]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")

