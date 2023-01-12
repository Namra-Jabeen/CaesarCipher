#  Assignment for Computas DK
This project is a solution for an assignment given by Computas Denmark.
There are two solutions in this project. `caesar_cipher_unicode.py` is based on unicode, and 
can only deal with the uppercase and lowercase English alphabet letters [A-Za-z].
`caesar_cipher_custom.py` can be extended to a custom alphabet (only letters), so e.g. the danish ÆØÅ can be added,
Other alternatives would be that the alphabet can be shuffled or shortened.

## Usage
Run the script the following way
```python
python3 caesar_cipher_unicode.py
```
or
```python
python3 caesar_cipher_custom.py
```

### Encryption
For encryption of text in textfile:
```bash
[KEY] [PATH-TO-FILE]
```
#####Example:
Input:
``` 
7 examples/plaintext.txt
```
Output:
```
Lewlyplujl pz aol alhjoly vm hss aopunz.
uv vul pz zv iyhcl aoha ol pz uva kpzabyilk if zvtlaopun bulewljalk p ohk yhaoly il mpyza pu h cpsshnl aohu zljvuk ha Yvtl.
tlu myllsf ilsplcl aoha dopjo aolf klzpyl,
P jhtl P zhd P jvuxblylk.
```

### Decryption
For decryption of text in textfile:
```bash
[KEY] [PATH-TO-FILE] -d
```
#####Example:
Input:
``` 
7 examples/ciphertext.txt -d
```
Output:
```
Experience is the teacher of all things.
no one is so brave that he is not disturbed by something unexpected i had rather be first in a village than second at Rome.
men freely believe that which they desire,
I came I saw I conquered.

```



## Disclaimer:
Both implementations do not include major error handling, as it was not included in the task.