# Algorithms
- step-by-step set of instructions for completing a task[problem solving]

## Off example:

Preparing Tea
### Antony's step

1. Boil the water
2. Add milk
3. Add coffee
4. Wait for it to boil
5. Ready to serve.

### Dorothy's step

1. Boil the water
2. Add milk
3. Add tea leaves
4. Weka kwa moto
5. Wait to boil
6. Add sugar
7. Ready to serve


# Characteristics

- Clear.
- Finite[can stop]
- Correct
- Efficient , should avoid reduntant sections
- It should have defined inputs and output

## Example of an algorithm

- You've been tasked to find the largest number in this list: [34, 78, 345, 90]

### algorithm
- describes the steps needed

```text

    1. Start ->
    2. Take first number from the list -> 
    3. Assume that the first no. is the largest. 
    4. Compare it with the next number -> 
    5. If the next number is bigger than the first number, we need to store it and remember it. 6. repeat until all the numbers in the list have been compared. ->
    7. Display the largest number
```

### Code
- Will tell the computer exactly how to perform the above steps

```python

   numbers = [34, 78, 345, 90]

   larget_number = numbers[0]

   for number in numbers:
    if number > largest_number:
        largest_number = number
    print(largest_number)

```

### Summary 

- ``Algorithm`` Plan, ``Code`` implementation of the plan.


# Sequence.
- A Collection of items arranged in specific order.

## Types Of Sequence
- ``List`` - A collection of multiple values stored in a specific/ordered collection. "Mutable"
- Tuple
- String
- Range


### mutable and immutable
- mutable - contents can be changed after creating the list
- immutable - cannot be changed

1. - ``List`` 
- A collection of multiple values stored in a specific/ordered collection. "Mutable"
- Can store different data types.

- Creation

scores = [5, 4, 4, 1]

- Adding an items to the list

scores.append(5)

- Reading values of a list
```python
scores[0] # 5
scores[3] # 1
```

- updating 
scores[0] = 3

- deleting

scores.pop()

