#!/usr/bin/python
# -*- coding: utf-8 -*-

SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    #replace this for solution
    text = ""
    if number >= 100:
        hun = int(number / 100)
        text += FIRST_TEN[hun - 1] + " hundred"
        number = number % 100
        if hun > 0 and number > 0:
            text += " "
    if number >= 20:
        ten = int(number / 10)
        text += OTHER_TENS[ten - 2]
        number = number % 10
        if number:
            text += " " + FIRST_TEN[number - 1]
    elif number >= 10:
        text += SECOND_TEN[number - 10]
    elif number > 0:
        text += FIRST_TEN[number - 1]
    return text


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
