numbers = [34, 78, 345, 90]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)