import random
from art import logo
print(logo)

def guessing():
    chances = chance
    while chances:
        print(f"You have {chances} chances to guess the number.")
        user_guess = int(input("Make a guess:"))
        if user_guess < comp_guess:
            chances -= 1
            print("Too low, guess again.")

        elif user_guess > comp_guess:
            chances -= 1
            print("Too high, guess again.")

        elif user_guess == comp_guess:
            print(f"You win! The correct answer is {user_guess}")
            break

        if chances == 0:
            print("\nGame over, better luck next time!")

while True:
    print("\nWelcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100~")

    guess_list = []
    for guess in range(0,100):                 #or use randint 🤷‍♀️
        guess_list.append(guess)
    comp_guess = random.choice(guess_list)

    user_choice = input("\nChoose a difficulty to play: Easy or Hard.\n").lower()

    if user_choice == "easy":
        chance = 10
        guessing()
    elif user_choice == "hard":
        chance = 5
        guessing()
    else:
        print("Enter valid response and try again.")

    again = input("Do you want to continue: yes or no.\n").lower()
    if again == "yes":
        continue
    elif again == "no":
        print("See you next time!")
        break
