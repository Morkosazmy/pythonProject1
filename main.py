import string
import random
from operator import index

chars = " " + string.digits + string.ascii_letters + string.punctuation

chars = list(chars)
keys = list.copy(chars)
#print(chars)
random.shuffle(keys)
#print(keys)

#Encryption
message = input("Enter a message to encrypt: ")
cipher_text = ""
for letter in message:
    index = chars.index(letter)
    cipher_text += keys[index] # smh :/
print(f"the encrypted message is : {cipher_text}")

#Decryption

secret_message = input("Enter the encrypted message here to decrypt it: ")
original_message = ""
for letter in secret_message:
    index = keys.index(letter)
    original_message += chars[index]
print(f"The original message is: {original_message}")

#Encryption and Decryption !
