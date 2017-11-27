#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import ceil
def total_cost(calls):
    costs = 0
    date_dur = {}
    for c in calls:
        dur = ceil(int(c.split(' ')[-1]) / 60)
        date = c.split(' ')[0]
        if date in date_dur:
            if date_dur[date] > 100:
                costs += dur * 2
            elif dur + date_dur[date] > 100:
                costs += 100 - date_dur[date] + 2 * (dur - (100 - date_dur[date]))
            else:
                costs += dur
            date_dur[date] += dur
        else:
            if dur > 100:
                costs += (dur - 100) * 2 + 100
            else:
                costs += dur
            date_dur[date] = dur
    return costs


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

