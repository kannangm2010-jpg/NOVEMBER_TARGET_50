"""
Binary Search Pyramid
Level: Easy
Question
Write a Python program to accept an odd integer N and print a numeric pattern containing N rows and N numbers in each row.

Each row must contain numbers that decrease toward the middle position and then increase.
 The middle number must be 1, and the numbers on either side must increase according to their distance from the middle.

Calculate the middle position using the binary search formula. Do not hardcode the pattern!!!!!!!!!.


Input:
5


Output:
3 2 1 2 3
3 2 1 2 3
3 2 1 2 3
3 2 1 2 3
3 2 1 2 3
"""

n=7
mid=(n)//2
c=0
while c<n+1:
    for i in range (mid,0,-1):
        print(i,end=" ")
    for j in range(2,mid+1,1):
        print (j,end=" ")
    print()        
    c+=1
