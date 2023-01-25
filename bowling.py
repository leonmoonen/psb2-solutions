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

def bowling_score(frames):
    score = 0
    frame_index = 0
    for frame in range(10):
        if frames[frame_index] == 'X':
            score += 10
            if frames[frame_index + 1] == 'X':
                score += 10
                if frames[frame_index + 2] == 'X':
                    score += 10
                else:
                    score += int(frames[frame_index + 2])
            else:
                score += int(frames[frame_index + 1])
                if frames[frame_index + 2] == '/':
                    score += 10 - int(frames[frame_index + 1])
                else:
                    score += int(frames[frame_index + 2])
            frame_index += 1
        elif frames[frame_index + 1] == '/':
            score += 10
            if frames[frame_index + 2] == 'X':
                score += 10
            else:
                score += int(frames[frame_index + 2])
            frame_index += 2
        else:
            score += int(frames[frame_index]) + int(frames[frame_index + 1])
            frame_index += 2
    return score

if __name__ == '__main__':
    frames = input()
    print(bowling_score(frames))
