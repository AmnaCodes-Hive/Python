#Using the Python Built in Random module
import random

#this is a function of python module
secret_number = random.randint(1 , 100)

#using loop (While True) it execute infinitely until we break it
while True:
    
    Guess = int(input("Guess the number (between 1 to 100):"))
    
    if Guess == secret_number:
        print("Congratulations🎉 you guessed it right")
        break
    elif Guess < secret_number:
        print("Too low You are very close Try one again😞")
    elif Guess > secret_number:
        print("Too High You are very close Try one again😖")
    else:
        print("Value Error Please enter a valid number!❌")
    
