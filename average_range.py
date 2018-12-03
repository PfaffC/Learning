import random
averages = []
for i in range(0,11):
    numbers = list(range(0,random.randint(1,101)))
    avg = sum(numbers)/len(numbers)
    averages.append(avg)
sorted(averages)
print(averages[len(averages)//2])
