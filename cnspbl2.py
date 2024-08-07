import tkinter as tk
import webbrowser
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

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username == "harshita" and password == encrypted_url:
        webbrowser.open_new(url)
    else:
        label_result.config(text="Invalid username or password")

root = tk.Tk()

label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_login = tk.Button(root, text="Login", command=check_credentials)
button_login.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
