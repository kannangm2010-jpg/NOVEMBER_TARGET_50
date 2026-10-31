"""
Find Angle MBCProblem Statement
:$ABC$ is a right triangle, at $90^\circ$ at $B$.
Therefore, $\angle ABC = 90^\circ$.
Point $M$ is the midpoint of hypotenuse $AC$.
You are given the lengths $AB$ and $BC$.
Your task is to find $\angle MBC$ (angle $MBC$, as shown in the original figure) in degrees.Input Format:
The first line contains the length of side $AB$.
The second line contains the length of side $BC$.Constraints:$0 < AB \le 100$$0 < BC \le 100$
Lengths $AB$ and $BC$ are natural numbers.Output Format:
Output $\angle MBC$ in degrees.Note: Round the angle to the nearest integer.
Examples:
If angle is $56.5000001^\circ$, then output $57^\circ$.
If angle is $56.5000000^\circ$, then output $57^\circ$.
If angle is $56.4999999^\circ$, then output $56^\circ$.Sample Input:10
10
Sample Output:45°
"""

import math

ab=int(input())
bc=int(input())
angle_rad = math.atan(ab / bc)
angle_deg = math.degrees(angle_rad)
result = round(angle_deg)
print(str(result) + chr(176))
