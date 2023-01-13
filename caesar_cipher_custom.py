def encrypt(plaintext,key,alphabet):
    output = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        if character in alphabet:
            output += get_shifted_character(character,key,alphabet)
        elif character in alphabet.lower():
            output += get_shifted_character(character,key,alphabet.lower())
        else:
            output += character
    return output

def decrypt(ciphertext,n,alphabet):
    return encrypt(ciphertext, len(alphabet)-n, alphabet)

# Auxiliary function
def get_shifted_character(character, key, alphabet):
    index = alphabet.find(character)
    new_index = (index + key) % len(alphabet)
    new_character = alphabet[new_index]
    return new_character

if __name__ == '__main__':
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # add/remove letters only
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
        print(decrypt(lines,key,alphabet))
    else:
        print(encrypt(lines,key,alphabet))