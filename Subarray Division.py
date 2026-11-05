"""
Problem: Subarray Division
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Sample Input:
5
1 2 1 3 2
3 2

Sample Output:
2

"""


#!/bin/python3

import math
import os
import random
import re
import sys



def birthday(s, d, m):
    p = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            p += 1
    return(p)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
