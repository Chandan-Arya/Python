print("Welcome to the computer quiz game")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

question: list[str] = [['cpu','central processing unit'],['gpu','graphic processing unit'],['ram','random access memory'],['rom','read only memory']]

print("Okay Let's Play :")
print("Write the full form of ....")

score: int = 0
for i in range(len(question)):
    # answer = input(f"What is {question[i][0].upper()} stands for? ").lower()
    answer = input(f"{question[i][0].upper()} : ").lower()
    if answer == question[i][1]:
        print("Correct! ")
        score+=1
    else: print("Incorrect!")

print(f"Your score {score}/{len(question)}  {score/len(question)*100}%")