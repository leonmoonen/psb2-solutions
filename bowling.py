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
if __name__ == '__main__':

	# input:
	# --------------------
	# output:
	# 0
	# input:
	# XXXXXXXXXXXX
	# output:
	# 300
	# input:
	# 5/5/5/5/5/5/5/5/5/5/5
	# output:
	# 150
	# input:
	# 7115XXX548/279-X53
	# output:
	# 145
	# input:
	# 532/4362X179-41447/5
	# output:
	# 100
	input_str = input()
	score = 0
	frame = 0
	first_bowl = True
	for i in range(len(input_str)):
		if input_str[i] == 'X':
			score += 10
			if frame < 9:
				if i+1 < len(input_str) and input_str[i+1] == 'X':
					score += 10
					if i+2 < len(input_str) and input_str[i+2] == 'X':
						score += 10
					elif i+2 < len(input_str):
						score += int(input_str[i+2])
				elif i+2 < len(input_str) and input_str[i+1] == '/':
					score += 10
				elif i+1 < len(input_str):
					score += int(input_str[i+1])
					if i+2 < len(input_str) and input_str[i+2] == '/':
						score += 10
					elif i+2 < len(input_str):
						score += int(input_str[i+2])
			frame += 1
			first_bowl = True
		elif input_str[i] == '/':
			score += 10
			if frame < 9:
				if i+1 < len(input_str) and input_str[i+1] == 'X':
					score += 10
				elif i+1 < len(input_str):
					score += int(input_str[i+1])
			frame += 1
			first_bowl = True
		elif input_str[i] == '-':
			if first_bowl:
				first_bowl = False
			else:
				frame += 1
				first_bowl = True
		else:
			score += int(input_str[i])
			if first_bowl:
				first_bowl = False
			else:
				frame += 1
				first_bowl = True
	print(score)
