#!/usr/bin/env python

from __future__ import division, print_function
import os
import sys
import random

SUGGESTION_FILE = '~/.imbored.config'

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

def load_suggestions(suggestion_file):
    suggestions = {}

    with open(suggestion_file) as sf:
        for line in sf:
            task, weight = line.split(':')
            suggestions[task.strip()] = float(weight)

    return suggestions

if __name__ == '__main__':
    suggestions = default_suggestions

    # load user-defined suggestions if the file exists
    user_suggestion_file = os.path.expanduser(SUGGESTION_FILE)
    if os.path.exists(user_suggestion_file):
        try:
            suggestions = load_suggestions(user_suggestion_file)
        except:
            print('Error loading ' + user_suggestion_file, file=sys.stderr)

    print(suggest(suggestions) + '?')
