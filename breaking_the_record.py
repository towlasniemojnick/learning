#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#Maria plays college basketball and wants to go pro.
# Each season she maintains a record of her play. She tabulates the
# number of times she breaks her season record for most points and
# least points in a game. Points scored in the first game establish
# her record for the season, and she begins counting from there.

def breakingRecords(scores):
    # Write your code here
    records = [scores[0],scores[0]]
    records_cnt= [0,0] #[max, min]
    for points in scores:
        if points > records[0]:
            records_cnt[0] = records_cnt[0] + 1
            records[0] = points
        elif points < records[1]:
            records_cnt[1] = records_cnt[1] + 1
            records[1] = points

    return records_cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
