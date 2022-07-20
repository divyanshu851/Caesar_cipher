from matplotlib import artist
from art import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt  :")

text = input("Type your Message :").lower()
shift = int(input("Type the shift number :"))


def caeser(sms, shift , cipher_direction):
    final_sms = ''

    if cipher_direction == "decode":
        shift *= -1

    for char in sms:
        char_index = alphabets.index(char)
        char_index += shift 
        final_sms += alphabets[char_index]
    
    print(f"Here's the {cipher_direction}d result : {final_sms}" )    


caeser(text, shift, direction)