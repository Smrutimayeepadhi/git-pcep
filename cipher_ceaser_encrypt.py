#video-64
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#hello 2
"""def encrypt(original_text, shift_amount):
    d = ""  # j

    for letter in original_text:
        alphabet_position = alphabet.index(letter) + shift_amount# 7 -> 9
        d += alphabet[alphabet_position] # j

    print(f"Here is the encoded result: {d}")
def decrypt(original_text, shift_amount):
    d = ""  # j

    for letter in original_text:
        alphabet_position = alphabet.index(letter) - shift_amount# 7 -> 9
        d += alphabet[alphabet_position] # j
    print(f"Here is the decoded result: {d}")    or"""
def ceaser(original_text, shift_amount, encode_or_decode):

    d = ""  # j
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        alphabet_position = alphabet.index(letter) + shift_amount  # 7 -> 9
        d += alphabet[alphabet_position]
        print(f"Here is the {encode_or_decode}d result: {d}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    msg = input("Type your message: ").lower()
    shift = int(input("Type your shift number: "))

    ceaser(original_text=msg, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again, otherwise type 'no': ")
    if restart == "no":
        should_continue = False
        print("goodbye!")





"""decrypt(original_text= msg, shift_amount= shift)
encrypt(original_text= msg, shift_amount= shift)"""





