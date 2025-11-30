import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

diagrams = {
    "rock":rock,
    "paper":paper,
    "scissors":scissors
}

result = ["rock","paper","scissors"]
user_choice = input("Your choice: rock,paper or scissors? ").lower()
print(diagrams[user_choice])
comp_choice = random.choice(result)
print(f"Computer's choice is: {comp_choice}")
print(diagrams[comp_choice])

if (user_choice=="rock" and comp_choice=="scissors") or (user_choice=="paper" and comp_choice=="rock") or (user_choice=="scissors" and comp_choice=="paper"):
    print("You win!")
elif (user_choice=="rock" and comp_choice=="rock") or (user_choice=="paper" and comp_choice=="paper") or (user_choice=="scissors" and comp_choice=="scissors"):
    print("It's a draw~")
else:
    print("Computer wins")
