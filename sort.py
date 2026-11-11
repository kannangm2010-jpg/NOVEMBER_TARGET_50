numbers = [94,96,97, 11, 12, 12, 22, 22, 25, 25, 64, 64]
print(numbers)
for i in (numbers):
    k=True
    for j in range(len(numbers)-1):
        if numbers[j]>numbers[j+1]:
                k=False
                numbers[j+1],numbers[j]=numbers[j],numbers[j+1]
    if k:
        break
print(numbers)
