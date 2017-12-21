#!/usr/bin/python
# -*- coding: utf-8 -*-

def cut_sentence(line, length):
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    # your code here
    result = ''
    print(line.split(' '))
    for w in line.split(' '):
        if len(result + w) < length:
            result += " " + w if result else w
        else:
            break
    if result != line and len(''.join(result.split(' '))) < length:
        result += "..."
    print(result)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')

