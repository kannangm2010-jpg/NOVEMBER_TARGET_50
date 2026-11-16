"""
Dry run
Initial list:

[64, 25, 12, 22, 11]
Pass	Smallest element	Swap	Result
1	11	64 ↔ 11	[11, 25, 12, 22, 64]
2	12	25 ↔ 12	[11, 12, 25, 22, 64]
3	22	25 ↔ 22	[11, 12, 22, 25, 64]
4	25	No change	[11, 12, 22, 25, 64]

What improved?
Metric	Program 1	Program 2
Comparisons	10	10
Swaps	Multiple possible	At most 4
Time complexity	O(n²)	O(n²)
"""
numbers = [94,96,97, 11, 12, 12, 22, 22, 25, 25, 64, 64]
for i in range(len(numbers)-1):
    m=i
    for j in range (i+1,len(numbers)):
        if numbers[m]>numbers[j]:
            m=j
    numbers[i], numbers[m] = numbers[m], numbers[i]
print(numbers)