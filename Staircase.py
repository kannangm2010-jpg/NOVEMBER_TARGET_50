"""
StaircaseProblem Statement:
Staircase detail:
This is a staircase of size $n = 4$:   #
  ##
 ###
####
Its base and height are both equal to $n$. It is drawn using # symbols and spaces. The last line is not precede
d by any spaces.
Write a program that prints a staircase of size $n$.Input Format:
A single integer, $n$, denoting the size of the staircase.Constraints:$0 < n \le 100$Output Format:
Print a staircase of size $n$ using # symbols and spaces.Sample Input:6
Sample Output:     #
    ##
   ###
  ####
 #####
######
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
   for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
