#!/usr/bin/python
# -*- coding: utf-8 -*-

def win(game_result,c):
        return any(all(c == i for i in j) for j in game_result + list(zip(*game_result))) \
            or all(c == game_result[i][i] for i in range(len(game_result))) \
            or all(c == game_result[i][len(game_result) - i - 1] for i in range(len(game_result)))
    
def checkio(game_result):
        if win(game_result, 'X'):
            return 'X'
        elif win(game_result, 'O'):
            return 'O'
        else:
            return 'D'
    #return "D" or "X" or "O"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
