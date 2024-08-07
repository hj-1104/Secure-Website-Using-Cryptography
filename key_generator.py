import string

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char in string.ascii_letters:
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

url = "https://www.techlistic.com/"
encrypted_url = caesar_cipher(url, 13)
print("Encrypted URL:", encrypted_url)
