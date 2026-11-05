"""
Problem: Day of the Programmer
Given a year, find the date of the 256th day of that year according to the official Russian calendar during that year.
 Print it in the format dd.mm.yyyy, where dd is the two-digit day, 
 mm is the two-digit month, and yyyy is the year.
(Note: Russia transitioned from the Julian to the Gregorian calendar in 1918).

Sample Input:
2017

Sample Output:
13.09.2017

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return("12.09."+str(year))
    else:
        return ("13.09."+str(year))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
