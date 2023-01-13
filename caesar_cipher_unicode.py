
# Encryption function using unicode
def encrypt(plaintext, key):
    alphabet_length = 26
    output = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        if character == " ":
            output += character
        elif character.isupper():
            output += get_shifted_character(character, key, alphabet_length, True)
        elif character.islower():
            output += get_shifted_character(character, key, alphabet_length, False)
        else:
            output += character
    return output

# Decryption function using the encryption function
def decrypt(ciphertext,key):
    alphabet_length = 26
    return encrypt(ciphertext,alphabet_length-key)

# Auxiliary  function
def get_shifted_character(character, key, alphabet_length, isUpper):
    # ord() takes a unicode character and returns the corresponding integer
    # chr() converts an integer to its unicode character and returns it.
    if isUpper == True:
       return chr((ord(character) + key - ord("A")) % alphabet_length + ord("A"))
    elif isUpper == False:
       return chr((ord(character) + key - ord("a")) % alphabet_length + ord("a"))

# For handling the entered input
if __name__ == '__main__':
    n = input()
    input = n.split(" ")
    decryption = False
    while("" in input):
        input.remove("")
    if len(input) >= 2:
        key = int(input[0])
        textfile = input[1]
    if len(input) > 2 and input[2]=="-d":
        decryption = True
    with open(textfile) as f:
        lines = f.read()
    if decryption == True:
        print(decrypt(lines,key))
    else:
        print(encrypt(lines,key))

