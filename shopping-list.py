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
Given a vector of ﬂoats representing the prices of various shopping goods and another vector of floats representing the percent discount of each of those goods, return the total price of the shopping trip after applying the discount to each item.
For example,
input:
1
50.0
1
100.0
output:
0.0
input:
1
50.0
1
10.0
output:
45.0
input:
2
20.0 20.0
2
100.0 50.0
output:
10.0
input:
2
20.0 20.0
2
20.0 0.0
output:
36.0
input:
3
10.0 20.0 30.0
3
5.0 10.0 95.0
output:
29.0
"""
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(float, input.split()))
    n = int(data[0])
    prices = data[1:(n + 1)]
    m = int(data[n + 1])
    discounts = data[(n + 2):]
    result = 0
    for i in range(n):
        result += prices[i] * (100 - discounts[i]) / 100
    print("{:.2f}".format(result))
