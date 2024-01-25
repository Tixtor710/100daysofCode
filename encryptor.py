import random
import string

chars =" "+ string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text= input("enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index= chars.index(letter)
    cipher_text+= key[index]

print(f"original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")

cipher_text= input("enter a message to decrypt: ")
plain_text= ""

for letter in cipher_text:
    index= key.index(letter)
    plain_text+= key[index]

print(f"encrypted Message: {cipher_text}")
print(f"Decrypted Message: {plain_text}")