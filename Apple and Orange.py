"""
Apple and Orange
Problem Statement:
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

The red region denotes the house, where 
s is the start point, and 
t is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.

Assume the trees are located on a single point, where the apple tree is at point 
a, and the orange tree is at point 
b.

When a fruit falls from its tree, it lands 
d units of distance from its tree of origin along the 
x-axis. A negative value of 
d means the fruit fell 
d units to the tree's left, and a positive value of 
d means it falls 
d units to the tree's right.   

Given the value of 
d for 
m apples and 
n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range 
[s,t]).   

Input Format:   

The first line contains two space-separated integers denoting the respective values of 
s and 
t.   

The second line contains two space-separated integers denoting the respective values of 
a and 
b.   

The third line contains two space-separated integers denoting the respective values of 
m and 
n.   

The fourth line contains 
m space-separated integers denoting the respective distances that each apple falls from point 
a.   

The fifth line contains 
n space-separated integers denoting the respective distances that each orange falls from point 
b.   

Constraints:
1≤s,t,a,b,m,n≤10 
5
 
−10 
5
 ≤d≤10 
5
 
a<s<t<b

Output Format:Print two integers on two different lines:   

The first integer: the number of apples that fall on Sam's house.   

The second integer: the number of oranges that fall on Sam's house.   

Sample Input:   

7 11
5 15
3 2
-2 2 1
5 -6
Sample Output:   

1
1
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    l=0
    p=0
    for i in range(len(apples)):
        apples[i]+=a
    
    for j in range(len(oranges)):
        oranges[j]+=b
    house = range(s, t + 1)
    for x in apples:
        if x in house:
            l+=1
    for k in oranges:
        if k in house:
            p+=1
    print(l)
    print(p)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
