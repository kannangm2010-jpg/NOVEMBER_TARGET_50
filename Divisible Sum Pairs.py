"""
Problem: Divisible Sum Pairs
Given an array of integers and a positive integer k, determine the number of (i, j)
 pairs where i < j and ar[i] + ar[j] is evenly divisible by k.

Sample Input:
6 3
1 3 2 6 1 2

Sample Output:
5

"""

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    pairs = combinations(ar, 2)
    valid_pairs = filter(lambda p: sum(p) % k == 0, pairs)
    return len(list(valid_pairs))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
