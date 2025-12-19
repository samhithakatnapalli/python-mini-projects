bids = {}

while True:
    name = input("Enter your name: ")
    price = int(input("Enter your price: $"))

    bids[name] = price
    user_choice = input("Are there any new bids to add:\n").lower()
    if user_choice == "yes":
        print("\n" * 100)
    elif user_choice == "no":
        break
    else:
        break

winner = max(bids, key = bids.get)
print(f"The highest bidder is {winner} with a bid of ${bids[winner]}")
