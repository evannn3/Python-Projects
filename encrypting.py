
import string
alphabet = string.ascii_lowercase
char = 'qwertyuiopasdfghjklzxcvbnm'

answer = input('Would you like to decrypt or encrypt?: ')

if answer == 'encrypt':                             #encrypting
    message = input('Please enter a message: ')
    encrypt_table = str.maketrans(alphabet, char) # combines both variable strings using strmaketrans
    encrypted = message.translate(encrypt_table) # binds message to encrypt_table
    print(f"Encrypted: {encrypted}")

if answer == 'decrypt':    #decrypting
    dmessage = input('Please enter a message: ')
    decrypt_table = str.maketrans(char, alphabet) # swapped alphabet and chars
    decmsg = dmessage.translate(decrypt_table)
    print(f"Decrypted: {decmsg}")
                                                 #ziol zgga lg ysohhofu sgfu gdr ufu

