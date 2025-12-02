import random
import hangman_words
import hangman_art

#logo for game
logo = hangman_art.logo
print(logo)

#ASCII art
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# word list
word_list = hangman_words.word_list
print(word_list)

# random word choosing
chosen_word = random.choice(word_list)

#placeholder for letters
placeholder = ''
for letter in range(len(chosen_word)):
    placeholder += ' _ '
print(placeholder)

#loop and its conditions
game_over = False
previous_guesses = []
lives = len(stages)

while not game_over:
    print(f" --- YOU HAVE {lives} LIVE(S) LEFT --- ")
    guess = input("Guess a letter: ").lower()

    if guess in previous_guesses:
        print("You've already guessed this letter.Try again")

    display = ''
    for letters in chosen_word:
        if letters == guess:
            display += guess
            previous_guesses += guess
        elif letters in previous_guesses:
            display += letters
        else:
            display += ' _ '
    print(display)

    if guess in chosen_word:
        print("Right")
    if guess not in chosen_word:
        print(f"You guessed {guess} which is not in the letter. You lose a life")
        lives -= 1
        print(stages[lives])
        
    #conditions to end loop
    if ' _ ' not in display:
        game_over = True
        print(" --- YOU WIN! --- ")
    if lives == 0:
        game_over = True
        print(" --- GAME OVER --- ")
