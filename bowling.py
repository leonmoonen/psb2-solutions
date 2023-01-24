import os
import sys
import numpy as np
import math
import datetime
import collections
import itertools
import queue
import re
"""
Given a string representing the individual bowls in a 10-frame round of 10 pin bowling, return the score of that round.
For example,
input:
--------------------
output:
0
input:
XXXXXXXXXXXX
output:
300
input:
5/5/5/5/5/5/5/5/5/5/5
output:
150
input:
7115XXX548/279-X53
output:
145
input:
532/4362X179-41447/5
output:
100
"""
def bowling_score(s):
    c = 0
    r = 0
    for x in s:
        if x == '/':
            r += 10 - c
            c = 0
        elif x == 'X':
            r += 10
            c = 0
        elif x == '-':
            r += 0
            c = 0
        else:
            r += int(x)
            c += int(x)
    return r

if __name__ == '__main__':
    s = 'XXXXXXXXXXXX'
    print(bowling_score(s))
