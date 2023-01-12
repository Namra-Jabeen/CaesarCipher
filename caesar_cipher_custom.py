def encrypt(plaintext,n,alphabet):
    output = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch in alphabet:
            idx = alphabet.find(ch)
            new_idx = (idx + n) % len(alphabet)
            new_char = alphabet[new_idx]
            output += new_char
        elif ch in alphabet.lower():
            idx = alphabet.find(ch.upper())
            new_idx = (idx + n) % len(alphabet)
            new_char = alphabet[new_idx]
            output += new_char.lower()
        else:
            output += ch
    return output

def decrypt(ciphertext,n,alphabet):
    return encrypt(ciphertext, len(alphabet)-n, alphabet)

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