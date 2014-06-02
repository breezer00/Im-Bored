#!/usr/bin/env python

from __future__ import division, print_function
import random

default_suggestions = {
    'read books': 5,
    'practice coding': 3,
    'read manga': 1,
    'watch dramas': 1,
}

def suggest(suggestions):
    """Return one of the suggestions based on weights.
    @param dict suggestions
    """
    weight_sum = sum(suggestions.values())
    prob_ranges = []
    lower_bound = 0.0

    # generate probability ranges
    for task, weight in suggestions.iteritems():
        upper_bound = lower_bound + weight / weight_sum
        prob_ranges.append((task, (lower_bound, upper_bound)))

        # update lower bound
        lower_bound = upper_bound

    rand_number = random.random()

    for task, (low, high) in prob_ranges:
        if low <= rand_number < high:
            return task

    raise AssertionError('Should not be here. O_O');

if __name__ == '__main__':
    print(suggest(default_suggestions) + '?')
