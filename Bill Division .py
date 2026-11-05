"""
Problem: Bill Division (Bon Appetit)
Two friends, Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct. If correct, print "Bon Appetit". Otherwise, print the integer amount of money that Brian owes Anna.

Sample Input:
4 1
3 10 2 9
12

Sample Output:
5
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    bill.pop(k)
    s=(reduce(lambda q,w:q+w,bill))/2
    if s==b:
        print("Bon Appetit")
    else:
        print(int(b-s))
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
