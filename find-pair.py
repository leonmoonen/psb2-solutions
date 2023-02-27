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
5
7
input:
2
2500 6352
8852
output:
2500
6352
input:
2
-14 5
-9
output:
-14
5
input:
2
40 -19
21
output:
40
-19
input:
2
-4 4
0
output:
-4
4
"""
if __name__ == '__main__':
    num_of_elements = int(input())
    vector = [int(x) for x in input().split()]
    target = int(input())
    for i in range(num_of_elements):
        for j in range(i+1, num_of_elements):
            if vector[i] + vector[j] == target:
                print(vector[i])
                print(vector[j])
                break
