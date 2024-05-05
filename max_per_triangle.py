#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    # need to find sticks that sum of two is bigger than the third
    # then sum up, and verify if it is bigger then the current max value

    current_max_sum = -1  # initialize the max value

    max_triangle = [-1,-1,-1]

    # we are looking for the maximum, therefore we need to have the longest first
    sticks.sort(reverse=True)

    for i in range(0, len(sticks)-2):
        if (sticks[i] < sticks[i + 1] + sticks[i + 2]) and (sticks[i + 1] < sticks[i] + sticks[i + 2]) and (sticks[i + 2] < sticks[i] + sticks[i + 1]):

            if sticks[i + 2]+ sticks[i+1]+ sticks[i] > current_max_sum:
                current_max_sum = sticks[i + 2]+ sticks[i+1]+ sticks[i]
                max_triangle[0] = sticks[i + 2]
                max_triangle[1] = sticks[i + 1]
                max_triangle[2] = sticks[i]
            else:
                print(sticks[i + 2], sticks[i+1], sticks[i])
        else:
            pass

    if current_max_sum == -1:
        return [-1]
    else:
        return max_triangle

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
