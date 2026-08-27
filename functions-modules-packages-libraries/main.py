from calculation import substract, twenty
from calculations.add import add
from calculations.multiply import multiply
from calculations.squareroot import findSquareRootOfGivenNumber, rounding_number_to_nearest_base_int
# def greet():
#     print("Hello there!")
    

# greet()

# # function with parameter

# def print_name(name, name2="George", name3="Mike"):
#     print(name)
    

# print_name("Levis")

# # function with  parameter and default value assigned

# def print_one(one=1):
#     print(one);
    
# print_one(2)


## Calculations

result = add(89, twenty)
substract_result = substract(67, 788)

print(result)
print(substract_result)

print(multiply(10, 10))

print(findSquareRootOfGivenNumber(121))

print(rounding_number_to_nearest_base_int(4.8))