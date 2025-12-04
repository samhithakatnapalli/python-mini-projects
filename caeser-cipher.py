from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1           
    for letter in original_text:     #in case you add any symbols or numbers in input like "hello!"
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifting_encode = alphabet.index(letter) + shift_amount
            shifting_encode %= len(alphabet)          #keeps the index within the List range ([0-25] in this case)
            cipher_text += alphabet[shifting_encode]
    print(f"Your {encode_or_decode}ed text is: {cipher_text}")

wanna_continue = True
while wanna_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ("encode","decode"):
        direction = input("Wrong input, try again.")      #incase user types something other than standard input
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(shift_amount=shift, original_text=text, encode_or_decode=direction)    #calling the function

    ask = input("Do you want to continue: yes or no? \n").lower()
    if ask == "no":
        wanna_continue = False     #loop ends
