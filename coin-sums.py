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
Given a number of cents, ﬁnd the fewest number of US coins (pennies, nickles, dimes, quarters) needed to make that amount, and return the number of each type of coin as a separate output.
For example,
input:
1
output:
1000
input:
2
output:
2000
input:
3
output:
3000
input:
4
output:
4000
input:
5
output:
0100
"""
if __name__ == '__main__':
    lst = [['Pennies','Nickles','Dimes','Quarters']]
    for i in range(1,6):
        lst.append([i*1000,i*2000,i*3000,i*4000])
    for i in range(1,6):
        print("input:")
        print(i)
        print("output:")
        print(lst[i])
