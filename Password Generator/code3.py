import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.upper_var = tk.IntVar()
        self.lower_var = tk.IntVar()
        self.digits_var = tk.IntVar()
        self.punc_var = tk.IntVar()
        self.length_var = tk.IntVar()

        self.upper_check = tk.Checkbutton(root, text="Uppercase Letters", variable=self.upper_var)
        self.lower_check = tk.Checkbutton(root, text="Lowercase Letters", variable=self.lower_var)
        self.digits_check = tk.Checkbutton(root, text="Digits", variable=self.digits_var)
        self.punc_check  = tk.Checkbutton(root,text="Punctuations: ",variable = self.punc_var)
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_entry = tk.Entry(root, textvariable=self.length_var)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.result_label = tk.Label(root, text="Your password will appear here.")

        self.upper_check.pack(anchor=tk.W)
        self.lower_check.pack(anchor=tk.W)
        self.digits_check.pack(anchor=tk.W)
        self.punc_check.pack(anchor=tk.W)
        self.length_label.pack(anchor=tk.W)
        self.length_entry.pack(anchor=tk.W)
        self.generate_button.pack(anchor=tk.W)
        self.result_label.pack()

    def generate_password(self):
        if not self.upper_var.get() and not self.lower_var.get() and not self.digits_var.get():
            self.result_label.config(text="Please select at least one option.")
            return

        length = self.length_var.get()
        if length <= 0:
            self.result_label.config(text="Password length must be greater than 0.")
            return

        character_set = ''
        if self.upper_var.get():
            character_set += string.ascii_uppercase
        if self.lower_var.get():
            character_set += string.ascii_lowercase
        if self.digits_var.get():
            character_set += string.digits
        if self.punc_var.get():
            character_set += string.punctuation

        password = ''.join(random.choice(character_set) for _ in range(length))
        self.result_label.config(text="Generated Password: " + password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
