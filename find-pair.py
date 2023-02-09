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
Given a vector of integers, return the two elements that sum to a target integer.
For example,
input:
2
5 7
12
output:
57
input:
2
2500 6352
8852
output:
25006352
input:
2
-14 5
-9
output:
-145
input:
2
40 -19
21
output:
40-19
input:
2
-4 4
0
output:
-44
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a = input().split(' ')
        b = int(input())
        for j in range(len(a)):
            for k in range(len(a)):
                if int(a[j]) + int(a[k]) == b:
                    print(int(a[j]) * int(a[k]))
