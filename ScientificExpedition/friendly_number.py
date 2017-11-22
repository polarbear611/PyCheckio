#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import log2, log10
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    power = powers[0]
    if 0 == number:
        power = 0
    #elif int(log10(base)) == log10(base):
    #    power = int(log10(abs(number)))
    #elif int(log2(base)) == log2(base):
    #    power = int(log2(abs(number)))
    elif 1000 == base:
        power = int(log10(abs(number)) / 3)
    elif 1024 == base:
        power = int(log2(abs(number)) / 10)
    elif 100 == base:
        power = int(log10(abs(number)) / 2)
    elif 10 == base:
        power = int(log10(abs(number)))
    elif 2 == base:
        power = int(log2(abs(number)))
    try:
        power_name = powers[power]
    except IndexError:
        power_name = powers[-1]
        power = len(powers) - 1
    number = number / pow(base, power)
    if decimals > 0:
        return "%.0{}f".format(decimals) % number + power_name + suffix
    else:
        return str(int(number)) + power_name + suffix    
    #print (number, power)
    
    #return str(number)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'


