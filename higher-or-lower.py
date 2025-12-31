import random
from art import logo,vs
from game_data import data

def try_again():
    score = 0
    guesses = None
    while True:
        a = random.choice(data) if guesses is None else guesses
        b = random.choice(data)
        while b == a:
            b = random.choice(data)

        followers_a = a['follower_count']
        followers_b = b['follower_count']

        print(logo)
        print(f"Compare A: {a['name']},{a['description']},{a['country']}")
        print(vs)
        print(f"Against B: {b['name']},{b['description']},{b['country']}")

        who_has_more = input("Who has more followers? A or B:\n").lower()
        winner = a if followers_a > followers_b else b
        correct_guess = 'a' if winner == a else 'b'

        if who_has_more == correct_guess:
            score += 1
            guesses = winner
            print(f"You guessed correctly! Your current score is {score}")
            continue
        else:
            print(f"Oops, wrong guess. Your final score is {score}")
            again = input("Do you wanna try again? Yes or No:").lower()
            if again == "yes":
                try_again()
            else:
                print("See ya next time!")
            return
        
try_again()
                score = 0
                guesses = None
                print("\n" *20)
            else:
                print("See ya next time!")
                try_again = False
