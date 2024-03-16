#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zeros = 0
    positives = 0
    negatives = 0

    for num in arr:
        if num > 0:
            positives = positives + 1
        elif num < 0:
            negatives = negatives + 1
        elif num == 0:
            zeros = zeros + 1

    print(round(positives/n,6))
    print(round(negatives/n,6))
    print(round(zeros/n,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)