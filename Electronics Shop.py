"""
Electronics Shop  
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a given budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return $-1$.   Example$b = 60$$keyboards = [40, 50, 60]$$drives = [5, 8, 12]$The person can buy a $40 \text{ keyboard} + 12 \text{ USB drive} = 52$, or a $50 \text{ keyboard} + 8 \text{ USB drive} = 58$. Choose the latter as the more expensive option and return $58$.Input FormatThe first line contains three space-separated integers $b$, $n$, and $m$: the budget, the number of keyboard models, and the number of USB drive models.The second line contains $n$ space-separated integers $keyboards[i]$, the prices of each keyboard model.The third line contains $m$ space-separated integers $drives[j]$, the prices of the USB drives.   Constraints$1 \le n, m \le 1000$$1 \le b \le 10^6$The price of each item is in the inclusive range $[1, 10^6]$.Output FormatPrint a single integer denoting the amount of money spent. If it is impossible to buy both items, print -1.Sample InputPlaintext10 2 3
3 1
5 2 8
Sample OutputPlaintext
9
"""
def getMoneySpent(keyboards, drives, b):
    m = -1
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                m = max(m, k + d)
    return m


