import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    user_choice = [random.choice(cards), random.choice(cards)]
    computer_choice = [random.choice(cards), random.choice(cards)]
    while True:
        user_sum = sum(user_choice)
        comp_sum = sum(computer_choice)
        print(f"Your hand: {user_choice}, Current sum: {user_sum}")
        print(f"Computer's first card: {computer_choice[0]}")

        if user_sum == 21 and len(user_choice)==2 and comp_sum == 21 and len(computer_choice) == 2:
            print(f"Computer hand: {computer_choice}")
            print("- Computer wins -")
            break

        elif comp_sum == 21 and len(computer_choice) == 2:
            print(f"Computer hand: {computer_choice}")
            print("- Computer wins -")
            break

        else:
            if user_sum > 21:
                if 11 in user_choice:
                    user_choice[user_choice.index(11)] = 1
                    user_sum = sum(user_choice)
                    if user_sum > 21:
                        print(f"Computer hand: {computer_choice}")
                        print("- Computer wins -")
                        break
                else:
                    print(f"Computer hand: {computer_choice}")
                    print("- Computer wins -")
                    break

            decision = input("Do you want to draw another card? yes or no:\n")
            if decision == "yes":
                user_choice.append(random.choice(cards))
            elif decision == "no":
                while comp_sum < 17:
                    computer_choice.append(random.choice(cards))
                    comp_sum = sum(computer_choice)
                if comp_sum > 21:
                    print(f"Computer hand: {computer_choice}")
                    print("- You win! -")
                    break

                else:
                    if user_sum > comp_sum:
                        print(f"Computer hand: {computer_choice}")
                        print("You win!")
                        break

                    elif comp_sum > user_sum:
                        print(f"Computer hand: {computer_choice}")
                        print("- Computer wins -")
                        break

                    elif user_sum == comp_sum:
                        print(f"Computer hand: {computer_choice}")
                        print(f"Sum is:\nUser sum: {user_sum}\nComputer sum: {comp_sum}")
                        print("Draw")
                        break

while input("\nDo you wanna play BlackJack? yes or no:\n") == "yes":
    blackjack()
else:
    print("See you next time~")
