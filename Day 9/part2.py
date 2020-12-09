from part1 import numbers, result

low_index = 0
high_index = 2

while high_index < len(numbers):
    range_of_values = numbers[low_index:high_index]
    consider = sum(range_of_values)
    if consider == result:
        break
    elif consider < result:
        high_index += 1
    elif consider > result:
        low_index += 1

print(range_of_values)
print(max(range_of_values) + min(range_of_values))

