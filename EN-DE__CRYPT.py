import tkinter as tk
from tkinter import PhotoImage
import sys
import threading
import time
import requests
from PIL import Image, ImageTk
from io import BytesIO

class Caesar_Cipher(tk.Frame):
    
    def __init__(self, root):
        self.color1 = 'black'
        self.color2 = '#00FF00'  # Lime
        self.color3 = 'white'
        self.color4 = 'red'      # Red

        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.num_letters = len(self.letters)

        super().__init__(root, bg=self.color1)

        self.button_encrypt_color = self.color2
        self.button_decrypt_color = self.color4

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)

        # Placeholder for the preloader
        self.loader_label = tk.Label(self.main_frame, bg=self.color1)
        self.loader_label.grid(column=0, row=0, pady=(100, 20))

        # Load the GIF from URL
        response = requests.get('https://media.tenor.com/DKSpwZW0AcsAAAAM/loading-money.gif')
        img_data = response.content
        self.image = Image.open(BytesIO(img_data))

        # Prepare the frames
        self.frames = []
        for i in range(self.image.n_frames):
            self.image.seek(i)
            frame = ImageTk.PhotoImage(self.image.copy().convert("RGBA").crop((0, 0, self.image.width, self.image.height)))
            self.frames.append(frame)

        # Create a label for the processing text
        self.processing_label = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color3,
            font=('Arial', 14),
            text='Launching The "  [ EN-DE__CRYPT |AWS| ]  " Application - Meanwhile have a sip of water  :)'
        )
        self.processing_label.grid(column=0, row=1, pady=(10, 20))  # Adjust the row as necessary

        self.show_preloader()

    def show_preloader(self):
        self.play_gif()  # Start playing the gif
        self.after(20000, self.start_main_application)  # Wait 2 seconds before transitioning

    def play_gif(self, frame_index=0):
        """Play the GIF frames."""
        self.loader_label.config(image=self.frames[frame_index])
        frame_index += 1
        if frame_index >= len(self.frames):
            frame_index = 0
        self.after(70, self.play_gif, frame_index)

    def start_main_application(self):
        self.loader_label.grid_forget()  # Hide the loader
        self.render_widgets()  # Show the main application widgets

    def render_widgets(self):
        self.title = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color3,
            font=('GodOfWar', 41, 'bold'),
            text='EN-DE __ CRYPT |AWS|'
        )
        self.title.grid(column=0, row=0, sticky=tk.EW, pady=35)

        self.text_widget = tk.Text(
            self.main_frame,
            bg=self.color2,
            fg=self.color1,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Harrington', 20),
            height=5,
            padx=10,
            pady=10,
            highlightthickness=0,
            border=7
        )
        self.text_widget.grid(column=0, row=1, padx=100)
        self.text_widget.bind("<KeyRelease>", self.on_key_release)

        self.key_label = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color3,
            font=('Elephant', 13),
            text=f'Key (1-{self.num_letters - 1})',
            justify=tk.CENTER
        )
        self.key_label.grid(column=0, row=2, pady=(38, 10))

        self.buttons_container = tk.Frame(self.main_frame, bg=self.color1)
        self.buttons_container.columnconfigure(0, weight=1)
        self.buttons_container.columnconfigure(1, weight=1)
        self.buttons_container.columnconfigure(2, weight=1)
        self.buttons_container.grid(column=0, row=3, sticky=tk.NSEW, padx=100)

        self.button_encrypt = tk.Button(
            self.buttons_container,
            bg=self.button_encrypt_color,
            fg=self.color3,
            activebackground=self.button_encrypt_color,
            activeforeground=self.color3,
            font=('Elephant', 15),
            text='Encrypt',
            width=6,
            height=1,
            cursor='hand1',
            highlightthickness=0,
            border=0,
            state=tk.NORMAL,
            command=self.encrypt_command
        )
        self.button_encrypt.grid(column=0, row=0, ipadx=5, ipady=5)

        self.button_decrypt = tk.Button(
            self.buttons_container,
            bg=self.button_decrypt_color,
            fg=self.color3,
            activebackground=self.button_decrypt_color,
            activeforeground=self.color3,
            font=('Elephant', 15),
            text='Decrypt',
            width=6,
            height=1,
            cursor='hand1',
            highlightthickness=0,
            border=0,
            state=tk.NORMAL,
            command=self.decrypt_command
        )
        self.button_decrypt.grid(column=2, row=0, ipadx=5, ipady=5)

        self.key_entry_validation_command = self.buttons_container.register(self.key_entry_validation)
        self.key_entry = tk.Entry(
            self.buttons_container,
            bg=self.color2,
            fg=self.color4,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Arial', 15),
            width=6,
            highlightthickness=0,
            border=0,
            justify=tk.CENTER,
            validate='key',
            validatecommand=(self.key_entry_validation_command, '%P')
        )
        self.key_entry.grid(column=1, row=0, ipady=9)

        self.message_label = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color3,
            font=('Arial', 20),
            text=""
        )
        self.message_label.grid(column=0, row=4, pady=20)

        self.footer_label = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color3,
            font=('Arial Rounded MT Bold', 10),
            text='© 2024 | ARSHAD WASIB SHAIK | All Rights Reserved.'
        )
        self.footer_label.grid(column=0, row=10, pady=(70, 20))

    def on_key_release(self, event):
        if self.text_widget.get("1.0", tk.END).strip():
            self.button_encrypt.config(state=tk.NORMAL)
            self.button_decrypt.config(state=tk.NORMAL)
        else:
            self.button_encrypt.config(state=tk.NORMAL, bg=self.button_encrypt_color)
            self.button_decrypt.config(state=tk.NORMAL, bg=self.button_decrypt_color)

    def encrypt_decrypt(self, text, mode, key):
        result = ""
        for char in text:
            if char in self.letters:
                index = (self.letters.index(char) + (key if mode == 'encrypt' else -key)) % self.num_letters
                result += self.letters[index]
            else:
                result += char
        return result
    
    def key_entry_validation(self, value):
        if value == '':
            self.button_decrypt['state'] = tk.DISABLED
            self.button_encrypt['state'] = tk.DISABLED
            return True
        
        try:
            value = int(value)
        except ValueError:
            return False
        
        if value <= 0 or value >= self.num_letters:
            return False

        self.button_decrypt['state'] = tk.NORMAL
        self.button_encrypt['state'] = tk.NORMAL

        return True

    def encrypt_command(self):
        key = self.key_entry.get()
        if key.isdigit():
            key = int(key)
            text = self.text_widget.get('1.0', tk.END)

            threading.Thread(target=self.run_encrypt, args=(text, key)).start()

    def run_encrypt(self, text, key):
        time.sleep(2)  # Simulate a delay
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', self.encrypt_decrypt(text, 'encrypt', key))

        self.button_encrypt.config(bg='red', activebackground='red')
        self.display_message("The Encryption Mechanism Is Successfully Encrypted Plaintext...", self.color2)

    def decrypt_command(self):
        key = self.key_entry.get()
        if key.isdigit():
            key = int(key)
            text = self.text_widget.get('1.0', tk.END)

            threading.Thread(target=self.run_decrypt, args=(text, key)).start()

    def run_decrypt(self, text, key):
        time.sleep(2)  # Simulate a delay
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', self.encrypt_decrypt(text, 'decrypt', key))

        self.button_decrypt.config(bg='lime', activebackground='lime')
        self.display_message("The Decryption Mechanism Is Successfully Decrypted Secretkey.", self.color4)

    def display_message(self, message, color):
        self.message_label.config(text=message, fg=color)
        self.after(3000, self.clear_message)

    def clear_message(self):
        self.message_label.config(text="")

# Main application setup
def main():
    operating_system = sys.platform
    root = tk.Tk()

    try:
        icon_image = tk.PhotoImage(file='F:/Udemy Practice programs and Login form code file/EN-DE__CRYPT Application Using Caesar Cipher Algorithm/Iconmage.png')
        root.iconphoto(True, icon_image)
    except Exception as e:
        print("Error setting icon:", e)

    root.title(' |AWS| EN-DE __ CRYPT ')
    root.geometry("1500x700")
    root.resizable(True, True)
    app = Caesar_Cipher(root)
    root.mainloop()

if __name__ == '__main__':
    main()
