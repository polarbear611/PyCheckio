#!/usr/bin/python
# -*- coding: utf-8 -*-

def counterclockwise(t):
    return [''.join(l) for l in list(zip(*t))[::-1]]

def clockwise(t):
    
    return [''.join(l[::-1]) for l in list(zip(*t))]

def crack(g, p):
    text = ""
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 'X':
                text += p[i][j]
    return text

def recall_password(cipher_grille, ciphered_password):
    if ciphered_password[0][0].isupper():
        rotate = counterclockwise
    else:
        rotate = clockwise
    text = ""
    text += crack(cipher_grille, ciphered_password)
    for i in range(3):
        cipher_grille = rotate(cipher_grille)
        text += crack(cipher_grille, ciphered_password)
    
    return text

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

