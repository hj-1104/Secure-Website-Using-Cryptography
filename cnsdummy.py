import tkinter as tk
from cryptography.fernet import Fernet
import base64

# Generate a key for encryption/decryption
key = Fernet.generate_key()

# Encrypt the website URL
url = "https://www.techlistic.com/"
cipher_suite = Fernet(key)
token = cipher_suite.encrypt(url.encode())
encrypted_url = base64.urlsafe_b64encode(token).decode()

# Create a GUI with a password entry field and a submit button
root = tk.Tk()
root.title("Password Protected URL")

password_label = tk.Label(root, text="Enter Password:")
password_entry = tk.Entry(root, show="*")
submit_button = tk.Button(root, text="Submit", command=lambda: check_password())

password_label.pack()
password_entry.pack()
submit_button.pack()

# Function to check the password and decrypt the URL
def check_password():
    password = password_entry.get().encode()
    cipher_suite = Fernet(key)
    token = base64.urlsafe_b64decode(encrypted_url.encode())
    decrypted_url = cipher_suite.decrypt(token).decode()
    if decrypted_url == url:
        print("Correct password!")
        # Open the URL in a web browser
        import webbrowser
        webbrowser.open(decrypted_url)
    else:
        print("Incorrect password!")

# Run the GUI
root.mainloop()
