"""
# Collections.OrderedDict()

An `OrderedDict` is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

## Task
You are the manager of a supermarket. 
You have a list of $N$ items together with their prices that consumers bought on a particular day. 
Your task is to print each `item_name` and `net_price` in order of its first occurrence.

* **item_name** = Name of the item.
* **net_price** = Quantity of the item sold multiplied by the price of each item.

## Input Format
The first line contains the number of items, $N$. 
The next $N$ lines contains the item's name and price, separated by a space.

## Constraints
* $0 < N \le 100$

## Output Format
Print the `item_name` and `net_price` in order of its first occurrence.

## Sample Input
```text
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

"""
from collections import OrderedDict
num_items = int(input())
ordered_dictionary = OrderedDict()
for i in range(num_items):
    data = input().split()
    price = int(data[-1])
    item_name = " ".join(data[:-1])
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] += price
    else:
        ordered_dictionary[item_name] = price
for item, net_price in ordered_dictionary.items():
    print(item, net_price)
