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
Take a string in kebab-case and convert all of the words to camelCase. Each group of words to convert is delimited by "-", and each grouping is separated by a space. For example: "camel-case example-test-string"-> "camelCase exampleTestString".
For example,
input:

output:

input:
nospaceordash
output:
nospaceordash
input:
two-words
output:
twoWords
input:
two words
output:
two words
input:
all separate words
output:
all separate words
"""
def camelCase(s):
    s = s.split(" ")
    output = []
    for word in s:
        if "-" in word:
            word = word.split("-")
            word = [word[0]] + [word[i].capitalize() for i in range(1, len(word))]
            word = "".join(word)
        else:
            word = word.capitalize()
        output.append(word)
    output = " ".join(output)
    return output

if __name__ == '__main__':
    print(camelCase("camel-case example-test-string"))
