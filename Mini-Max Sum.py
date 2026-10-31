"""
Mini-Max SumProblem Statement:
Given five positive integers, find the minimum and maximum values that can be calculated
 by summing exactly four of the five integers. Then print the respective minimum and maximum values as a
  single line of two space-separated long integers.Input Format:
A single line of five space-separated integers.Constraints:$1 \le arr[i] \le 10^9$Output Format:
Print two space-separated long integers denoting the respective minimum and maximum values that
 can be calculated by summing exactly four of the five integers. (The output can be greater than a 32-bit integer.)
Sample Input:1 2 3 4 5
Sample Output:10 14
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    m=reduce(lambda x,c:x+c,arr[0:4])
    ma=reduce(lambda x,c:x+c,arr[1:5])
    print(m,ma)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
