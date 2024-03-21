#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# Given five positive integers, find the minimum and maximum values that can be calculated by
# summing exactly four of the five integers. Then print the respective minimum and maximum
# values as a single line of two space-separated long integers

def miniMaxSum(arr):
    sums = []
    for i in range(0, len(arr)):
        sums.append(sum(arr) - arr[i])

    print(f'{min(sums)} {max(sums)}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
