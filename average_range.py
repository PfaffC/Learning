import random
averages = []
for i in range(0,11):
    numbers = list(range(0,random.randint(1,101)))
    averages.append(sum(numbers)/len(numbers))
sorted(averages)
print(averages[len(averages)//2])
