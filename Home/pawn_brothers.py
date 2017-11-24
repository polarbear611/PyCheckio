#!/usr/bin/python
# -*- coding: utf-8 -*-

def safe_squares(square):
    if square[1] == '1':
    	return None
	if square[0] == 'a':
		return ['b' + str(int(square[1]) - 1)]
    if square[0] == 'h':
        return ['g' + str(int(square[1]) - 1)]
    return [chr(ord(square[0]) + 1) + str(int(square[1]) - 1), chr(ord(square[0]) - 1) + str(int(square[1]) - 1)]
    
def safe_pawn(pawn, pawns):
    try:
        for sq in safe_squares(pawn):
            if sq in pawns:
                return True
    except TypeError:
        print(pawn, safe_squares(pawn))
        return False
    return False

def safe_pawns(pawns):
    for p in pawns:
        print(safe_squares(p))
    return len([p for p in pawns if safe_pawn(p, pawns)])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

