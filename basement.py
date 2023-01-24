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
Given a vector of integers, return the ﬁrst index such that the sum of all integers from the start of the vector to that index (inclusive) is negative.
For example,
input:
1
-1
output:
0
input:
1
-100
output:
0
input:
2
-1 100
output:
0
input:
2
-95 100
output:
0
input:
2
-30 5
output:
0
"""
if __name__ == '__main__':
    n = int(input())
    input_str = input()
    input_list = input_str.split()
    input_int = [int(i) for i in input_list]
    sum = 0
    index = 0
    for i in input_int:
        sum += i
        if sum < 0:
            print(index)
            break
        index += 1
