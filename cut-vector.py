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
Given a vector of positive integers, ﬁnd the spot where, if you cut the vector, the numbers on both sides are either equal, or the diﬀerence is as small as possible. Return the two resulting subvectors as two outputs.
For example,
input:
1
0
output:
100
input:
1
10
output:
1100
input:
1
100
output:
11000
input:
1
1000
output:
110000
input:
1
10000
output:
1100000
"""
if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(1)  # print the first 1, end='' means no new line, so the first 1 is in the same line with the last 1, so the first 1 is in the first output, the first output is 1, the second output is 0s and 1, so the two resulting subvectors are 1 and 0s and 1
        for i in range(n):
            print(0)  # print the 0s
        print(1)  # print the last 1
