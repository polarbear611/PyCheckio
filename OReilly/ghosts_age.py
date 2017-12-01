#!/usr/bin/python
# -*- coding: utf-8 -*-

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = a + b, a
        
def checkio(opacity):
    opa = 10000
    age = 0
    f = fib()
    nextf = next(f)
    while(opa != opacity):
        age += 1
        if age < nextf: opa += 1
        elif age == nextf:
            opa -= age
            nextf = next(f)

    return age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
