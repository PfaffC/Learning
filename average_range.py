import random
averages = []
for i in range(0,11):
    random_n = random.randint(1,101)
    numbers = list(range(0,random_n))
    avg = sum(numbers)/len(numbers)
    averages.append(avg)
sorted(averages)
print(averages[len(averages//2)])