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
Peter has an n-sided die and Colin has an m-sided die. If they both roll their dice at the same time, return the probability that Peter rolls strictly higher than Colin.
For example,
input:
1
2
output:
0.0
input:
2
1
output:
0.5
input:
99
100
output:
0.49
input:
100
99
output:
0.5
input:
1
100
output:
0.0
"""
if __name__ == '__main__':
    n = input()
    m = input()
    p = 0
    for i in range(1, int(n) + 1):
        for j in range(1, int(m) + 1):
            if i > j:
                p += 1
    print(round(p / (int(n) * int(m)), 7))
