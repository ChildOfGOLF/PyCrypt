import os

def generate_key():
    import string
    import random

    chars = string.ascii_letters + string.digits + string.punctuation + ' \n'
    shuffled_chars = list(chars)
    random.shuffle(shuffled_chars)

    encrypt_dict = {c: shuffled_chars[i] for i, c in enumerate(chars)}
    decrypt_dict = {shuffled_chars[i]: c for i, c in enumerate(chars)}

    return encrypt_dict, decrypt_dict

def encrypt_file(input_file_path, output_file_path, encrypt_dict):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    encrypted_text = ''.join(encrypt_dict.get(c, c) for c in text)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

def decrypt_file(input_file_path, output_file_path, decrypt_dict):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    decrypted_text = ''.join(decrypt_dict.get(c, c) for c in text)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(decrypted_text)

def main():
    input_file_path = 'input.txt'
    encrypted_file_path = 'encrypted.txt'
    decrypted_file_path = 'decrypted.txt'

    encrypt_dict, decrypt_dict = generate_key()

    encrypt_file(input_file_path, encrypted_file_path, encrypt_dict)
    print(f'File {input_file_path} encrypted to {encrypted_file_path}')

    decrypt_file(encrypted_file_path, decrypted_file_path, decrypt_dict)
    print(f'File {encrypted_file_path} decrypted to {decrypted_file_path}')

if __name__ == "__main__":
    main()
