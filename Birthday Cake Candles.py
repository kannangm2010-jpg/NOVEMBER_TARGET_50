"""
Birthday Cake CandlesProblem Statement:
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.Example:$candles = [4, 4, 1, 3]$
The maximum height candles are $4$ units high. There are $2$ of them, so return $2$.   Input Format:The first line contains a single integer, $n$, the size of $candles[]$.The second line contains $n$ space-separated integers, where each integer $i$ describes the height of $candles[i]$.   Constraints:$1 \le n \le 10^5$$1 \le candles[i] \le 10^7$Output Format:Return the number of candles that are tallest.   Sample Input:   4
3 2 1 3
Sample Output:   2
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    
    candles.sort(reverse=True)
    s=0
    for i in range(len(candles)):
        if candles[0]==candles[i]:
            s+=1
    return s  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
