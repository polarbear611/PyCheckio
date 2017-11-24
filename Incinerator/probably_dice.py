#!/usr/bin/python
# -*- coding: utf-8 -*-

def number_count(dice_number, sides, target):
    if target < dice_number or target > sides * dice_number:
        return 0
    if dice_number == 1:
        return 1
    else:
        counts = [0 for i in range(dice_number, sides * dice_number + 1)]
        for i in range(sides):
            counts[i] = 1
        for dn in range(2, dice_number + 1):
            for s in range(dn * sides, dn - 1, -1):
                counts[s - dn] = sum([counts[s - i - (dn - 1)] if (s - i - (dn - 1)) >= 0 else 0 for i in range(1, sides + 1)])

        return counts[target - dice_number]

def probability(dice_number, sides, target):
    if target < dice_number or target > sides * dice_number:
        return 0.0
    total_pbt = pow(sides, dice_number)
    num_count = number_count(dice_number, sides, target)

    return float(num_count) / total_pbt


if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

