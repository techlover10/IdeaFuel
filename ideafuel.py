#!/usr/bin/python3
#
# Copyright © 2017 jared <jared@jared-devcenter>
#

import random

nouns = open('nouns.txt', 'r').readlines()
disruptive = open('disruptive.txt', 'r').readlines()

SIMPLE_CAT = True

NUM_IDEAS = 300

ret_words = []

for i in range(NUM_IDEAS):
    matched = False
    if not SIMPLE_CAT:
        while not matched:
            curr_word = random.choice(nouns).strip()
            found_tech = random.choice(disruptive).strip()
            first_char = found_tech[0]
            last_char = found_tech[-1]
            match_idx_first = curr_word.rfind(first_char)
            match_idx_last = curr_word.find(last_char)
            if match_idx_first > (len(curr_word) * 2)/3:
                matched = True
                ret_words.append(curr_word[0:match_idx_first] + first_char.upper() + found_tech[1:])
            elif match_idx_last < len(curr_word)/3 and len(curr_word) > 8:
                matched = True
                ret_words.append(found_tech[:-1]+ last_char.upper() + curr_word[match_idx_last:])
    else:
        a = random.randint(0, 1)
        if a == 0:
            tech = random.choice(disruptive).strip()
            ret_words.append(random.choice(nouns).strip().capitalize() + tech[0].upper() + tech[1:])
        else:
            ret_words.append(random.choice(disruptive).strip() + random.choice(nouns).strip().capitalize())

            

print(ret_words)

