
# cleaning function - To get rid of anything other than uppercase/lowercase letters and spaces.
# This is not necessary as the encryption and decryption function works regardless.
def cleaning(raw_text):
    cleaned_text = ""
    for i in range(len(raw_text)):
        ch = raw_text[i]
        if (ch == " " or ch.islower() or ch.isupper()):
           cleaned_text += ch
    return cleaned_text


# Encryption function using unicode
def encrypt(plaintext, n):
    output = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            output += ch
        elif ch.isupper():
            shifted_character_upper = (ord(ch) + n-65) % 26 + 65
            # ord() takes a unicode character and returns the corresponding integer
            # 65 is the integer for the unicode character "A". 65-90 are the integers for A-Z.
            output += chr(shifted_character_upper) #chr() converts an integer to its unicode character and returns it.
        elif ch.islower():  # if we know data is cleaned, we can replace elif with else and remove the else statement below.
            shifted_character_lower = (ord(ch) + n-97) % 26 + 97
            #97 is the integer for the unicode character "a". 97-122 are the integers representing a-z.
            output+= chr(shifted_character_lower)
        else:
            output+= ch
    return output

def decrypt(ciphertext,n):
    return encrypt(ciphertext,26-n)

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

