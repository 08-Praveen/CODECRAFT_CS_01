alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():  
            position = alphabet.index(char.lower()) 
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position] if char.islower() else alphabet[new_position].upper()
        else:
            cipher_text += char  
    print(f"Here's the text after encryption: {cipher_text}")

def decryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            position = alphabet.index(char.lower())
            new_position = (position - shift_key) % 26
            cipher_text += alphabet[new_position] if char.islower() else alphabet[new_position].upper()
        else:
            cipher_text += char 
    print(f"Here's the text after decryption: {cipher_text}")
end = False
while not end:

    To_do = input("Type 'encrypt' for the encryption process, type 'decrypt' for the decryption process: ").lower()
    text = input("Type your message:\n")
    shift = int(input("Enter shift key:\n"))

    if To_do == "encrypt":
        encryption(text, shift)
    elif To_do == "decrypt":
        decryption(text, shift)
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
    again = input("Type 'yes' to continue, Type 'no' to end\n")
    if again.lower() == 'no':
        end = True
        print("Goodbye!")