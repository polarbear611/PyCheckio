#!/usr/bin/python
# -*- coding: utf-8 -*-

def leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    leaps = int((year - 1) / 4) - int ((year - 1) / 100) + int((year - 1) / 400)
    
    if not leap(year):
        return [weekdays[(year + leaps + 6) % 7]]
    elif weekdays[(year + leaps + 6) % 7] == 'Sunday':
        return ['Monday', 'Sunday']
    else:
        return [weekdays[(year + leaps + 6) % 7], weekdays[(year + leaps + 7) % 7]]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"

