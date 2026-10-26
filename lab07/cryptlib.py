def encrypt(message, shift):
    encrypted_message = ""

    for character in message:
        if character.isalpha():
            if character.isupper():
             start = ord("A")
        else:
            start = ord("a")

        position = ord(character) - start
        new_position = (position + shift) % 26
        new_character = chr(start + new_position)
        encrypted_message += new_character
    else:
        encrypted_message += character

    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift) 

