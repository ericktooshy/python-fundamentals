# == equal operator
# = assignment

# No. guessing game

# - operators
# - control flow (if, if else)
# - while loop

secret_number = 7

# something that will enable us to get text from the user. input(), works like prompt


# method you used to change string number to real number in js is parseInt, in python it's int()


# comparison operator
# while loop => block of code that repeats certain instructions as long a certain condition remains true


guessed_number = 0

while guessed_number != secret_number:
    guessed_number = int(input("What's your lucky number: "))
    print("You guessed: ", guessed_number)

    if guessed_number == secret_number:
        print("You've won")
    elif guessed_number > secret_number:
        print("Number slightly higher, guess again")
    elif guessed_number < secret_number:
        print("Number slightly lower, guess again")
    else:
        print("Not correct expectation")
        
        


    


