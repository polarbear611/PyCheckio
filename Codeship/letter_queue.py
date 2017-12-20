#!/usr/bin/python
# -*- coding: utf-8 -*-

def letter_queue(commands):
    result = []
    for c in commands:
        if c.startswith('PUSH'):
            result.append(c[-1])
        else:
            try:
                result = result[1:]
            except:
                pass
    
    return "".join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
    assert letter_queue(()) == "", "Nothing"

    print("All done? Earn rewards by using the 'Check' button!")

