import random
from art import logo,vs
from game_data import data

score = 0
guesses = None
while True:
    if guesses is None:
        a = random.choice(data)
    else:
        a = guesses
    b = random.choice(data)

    count_a = (a['follower_count'])
    count_b = (b['follower_count'])

    print(logo)
    print(f"Compare A: {a['name']}, {a['description']} ,{a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']} ,{b['country']}.")

    who_has_more = input("Who has more followers? Type A or B:\n").lower()
    correct_answer = a if count_a > count_b else b
    correct_input = "a" if correct_answer == a else "b"

    if who_has_more == correct_input:
        score += 1
        print(f"You guessed right! Your current score is: {score}")
        guesses = correct_answer
        continue
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
