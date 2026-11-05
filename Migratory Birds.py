"""
Problem: Migratory Birds
Given an array of bird sightings where every element represents 
a bird type id, determine the id of the most frequently sighted type.
 If more than 1 type has been spotted that maximum amount, return the smallest of their ids. 
 It is guaranteed that each type is 1, 2, 3, 4, or 5.

Sample Input:
6
1 4 4 4 5 3

Sample Output:
4

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    c=0
    a=0
    for i in sorted(set(arr)):
        d=arr.count(i)
        if d>c:
            c=d
            a=i
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    







