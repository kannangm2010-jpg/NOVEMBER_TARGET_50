"""
Write a Python program to accept an odd integer N and print a centered diamond pattern containing numbers.

The diamond must have N rows. The first row contains one number, the next row contains three numbers, and the number of values increases by two until the middle row contains N numbers. After the middle row, the number of values decreases by two until the last row contains one number.

In each row, the numbers must decrease toward 1 at the center and then increase symmetrically. Use the midpoint logic associated with binary search to determine the center of the pattern.

Input:
5


Output:
    1
  2 1 2
3 2 1 2 3
  2 1 2
    1
"""
n = int(input("Enter an odd integer N: "))
mid = n // 2

for i in range(n):
    for j in range(n):
        # Calculate distance from the center of the grid
        if abs(i - mid) + abs(j - mid) <= mid:
            # Number is based on distance from the center column
            val = abs(j - mid) + 1
            print(val, end=" ")
        else:
            # Print spaces outside the diamond shape
            print(" ", end=" ")
    print()