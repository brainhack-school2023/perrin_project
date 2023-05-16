# import argparse
# import useful_functions 

# if __name__ == "__main__":

#     parser = argparse.ArgumentParser()
#     parser.add_argument('-i', help='path to the input text file containing the message')
#     parser.add_argument('-o', help='path for the output file where the processed message will be written')
#     parser.add_argument('-k', help=' string containing the key')
#     parser.add_argument('-m', help='mode, i.e., string that can take the value "encryption" or "decryption" to tell the script if you want to encrypt or decrypt the input message')
#     args = parser.parse_args()

#     with open(args.i, "r") as f:
#         message = f.read()
#     encrypt = args.m == "encryption"
#     new_message = useful_functions.process_message(message, args.k, encrypt)
#     with open(args.o, "w") as f:
#         message = f.write(new_message)

# # python cypher_script.py -i msg_file.txt -o msg_encrypted.txt -k my_key -m encryption
# # python cypher_script.py -i message_encrypted.txt -o msg_decrypted.txt -k my_super_secret_key -m decryption


import argparse
from useful_functions import process_message

def main(input_path, key, mode, output_path):
    with open(input_path, "r") as message_file:
        message = message_file.read()
    encrypt = mode == "encryption"
    processed_message = process_message(message, key, encrypt)
    with open(output_path, "w") as out_file:
        message = out_file.write(processed_message)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', 
                        dest="input_path",
                        type=str,
                        required=True,
                        help='Path to the input file.')
    parser.add_argument('-o',
                        dest="output_path",
                        type=str,
                        required=True, 
                        help='Path to the output file.')
    parser.add_argument('-k',
                        dest="key",
                        type=str,
                        required=True, 
                        help='Key.')
    parser.add_argument('-m', 
                        dest="mode",
                        type=str,
                        required=True,
                        choices=["encryption", "decryption"],
                        help='Wether to encrypt or decrypt the message.')
    args = parser.parse_args()
    main(args.input_path, args.key, args.mode, args.output_path)

    

# python cypher_script.py -i msg_file.txt -o msg_encrypted.txt -k my_key -m encryption
# python cypher_script.py -i message_encrypted.txt -o msg_decrypted.txt -k my_super_secret_key -m decryption