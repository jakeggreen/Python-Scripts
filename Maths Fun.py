combinations = []
values = []
dice_roll = []
probability = []

import graphlib

for n in range (1,7):
    for y in range (1,7):
        combinations.append(n + y)

for x in range (1,13):
    dice_roll.append(x)
    values.append(combinations.count(x))

for z in values:
    probability.append(int((z/sum(values))*100))

print(combinations)
print(dice_roll)
print(values)
print(probability)



