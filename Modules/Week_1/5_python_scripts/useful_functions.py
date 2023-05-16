def encrypt_letter(letter, key):
    encrypted_index = (ord(letter) + ord(key)) % 1114112
    return(chr(encrypted_index))

# print(encrypt_letter('l', 'h'))

def decrypt_letter(letter, key):
    decrypted_index = (ord(letter) - ord(key)) % 1114112
    return(chr(decrypted_index))

# print(decrypt_letter('Ô', 'h'))

def process_message(message, key, encrypt):
    """
    Inputs:
        message (str): message to encrypt/decrypt
        key (str): key used to encrypt/decrypt
        encrypt (bool): mode, i.e. encryption or decryption
    """
    new_message = ''
    process_letter = encrypt_letter if encrypt else decrypt_letter
    for i, letter in enumerate(message):
        k = key[i % len(key)]
        new_message += process_letter(letter, k)
        
    return(new_message)

# print(process_message('coucou', 'clef', True))
# print(process_message('ÆÛÚÉÒá', 'clef', False))

message = 'word'
key = 'key'

if __name__ == "__main__":
    encrypted_msg = process_message(message, key, True)
    decrypted_msg = process_message(encrypted_msg, key, False)
    if message == decrypted_msg:
        print('Test passed')
    else:
        print('Test failed')
