print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

user_choice = input("You're at a cross road. Where do you wanna go?\n   Type 'Left' or 'Right': ")
print(user_choice)
if user_choice == "Left":
    second_choice = input("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    print(second_choice)
    if second_choice == "swim":
        print("You've drowned.")
    else:
        third_choice = input("You arrive at the island unharmed. There's a house with 3 doors.\n   One red, one yellow and one blue. Which color do you choose?")
        print(third_choice)
        if third_choice == "red":
            print("Oops, red is for danger. Game over.")
        elif third_choice == "yellow":
            print("Ohh a safe choice indeed. You're safe.")
        else:
            print("Eh, blue isn't as safe as yellow. Game over.")
else:
    print("Game over. dun dun dun")
