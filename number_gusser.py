import random

user_range = int(input("Type the range of number : ")) # takeing the range of user
print(f"Guess a number between 1-{user_range}? ")

random_number = random.randint(1,user_range)

times = 0   # user gussed in how many number of times 
while True:

    # taking user input guessed number
    guessed_number = int(input("Guess number : "))
    times+=1    # increment each time

    # matching the guessed number
    if guessed_number == random_number:
        print(f"Wow! You got it! in {times} guesses")
        # quit()
        break   # right answer break out the loop
    elif guessed_number < random_number:
        print("Guess a larger number ")
    else:
        print("Guess a smaller number ")
        continue