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
Given a positive integer, square each digit and concatenate the squares into a returned string.
For example,
input:
0
output:
0
input:
1
output:
1
input:
2
output:
4
input:
3
output:
9
input:
4
output:
16
"""
if __name__ == '__main__':
    a = int(input())
    l = list(str(a))
    for i in range(len(l)):
        l[i] = int(l[i])
    for i in range(len(l)):
        l[i] = l[i] ** 2
    for i in range(len(l)):
        l[i] = str(l[i])
    print("".join(l))
