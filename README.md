# Caesar-Cipher-Encryption-Tool
A secure and user-friendly desktop application built with Python and Tkinter for performing encryption and decryption using the classical Caesar Cipher algorithm. This project features a modern graphical interface, multi-threading to prevent UI freezing, and serves as an educational tool for understanding foundational cryptography concepts.

## This project created by Arshad Wasib Shaik

### Execution Proof

https://github.com/user-attachments/assets/6e4dcc06-39e4-485f-a3e2-b3c2666e376a

## 🚀 Features

- **Graphical User Interface (GUI):** Built with Tkinter for an intuitive user experience.
- **Core Algorithm Implementation:** Encrypts and decrypts text using the Caesar Cipher method with a user-defined key.
- **Multi-threading:** Prevents the UI from freezing during encryption/decryption processes.
- **Modern UI Elements:** Includes a preloader animation and visual feedback for user actions.
- **Educational Value:** Clean, commented code perfect for students and developers learning about cryptography or GUI development in Python.

## 🛠️ Technologies Used

*   **Programming Language:** Python
*   **GUI Framework:** Tkinter
*   **Concurrency:** `threading` Library
*   **Image Processing:** PIL (Pillow)
*   **HTTP Requests:** `requests` Library

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/caesar-cipher-encryption-tool.git
    cd caesar-cipher-encryption-tool
    ```

2.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Create a `requirements.txt` file with: `requests` and `pillow`)*

3.  **Run the application:**
    ```bash
    python caesar_cipher.py
    ```

## 🎯 Usage

1.  Launch the application to see a preloader animation.
2.  Enter the text you wish to encrypt or decrypt into the main text box.
3.  Input a numerical key between 1 and 25.
4.  Click the **'Encrypt'** (green) button to encrypt the text.
5.  Click the **'Decrypt'** (red) button to decrypt the text.
6.  The result will appear instantly in the text box, with a confirmation message.


## 📸 Screenshots
<img width="1907" height="1039" alt="image" src="https://github.com/user-attachments/assets/28dd15ef-2b44-4cff-8049-f966ec65944e" />

<img width="1919" height="1043" alt="image" src="https://github.com/user-attachments/assets/32ad96b7-0744-43f3-abc9-90466fa6dfb6" />

<img width="1919" height="1046" alt="image" src="https://github.com/user-attachments/assets/02acd4e3-f63b-444a-b8d4-ab5a97649791" />

<img width="1919" height="1047" alt="image" src="https://github.com/user-attachments/assets/0b7bda84-05ff-47de-92df-1aa1bdb61f38" />

<img width="1919" height="1046" alt="image" src="https://github.com/user-attachments/assets/8c1a2bbf-b9f6-44c0-af8b-496d02f2b7c6" />

<img width="1919" height="1043" alt="image" src="https://github.com/user-attachments/assets/bb860777-3d27-4ab8-b62f-485151f4a3d6" />

<img width="1919" height="1044" alt="image" src="https://github.com/user-attachments/assets/42011624-257e-4b02-9be7-19bc28a0b5e0" />

<img width="1919" height="1042" alt="image" src="https://github.com/user-attachments/assets/0d407dc6-45af-4679-80fe-0fb87cb41b52" />

<img width="1919" height="1043" alt="image" src="https://github.com/user-attachments/assets/8369a149-163e-4efd-a4a8-aab45c6ce139" />

<img width="1919" height="1044" alt="image" src="https://github.com/user-attachments/assets/d6ebcfb4-365d-4dc2-a6fe-67b930d8a473" />

<img width="1919" height="1043" alt="image" src="https://github.com/user-attachments/assets/09ef9320-c04e-43da-93b6-90d4f6fa3d4c" />

## 🎯 Code Explanation
A secure and user-friendly **Python GUI application** built with **Tkinter** for performing encryption and decryption using the classical **Caesar Cipher algorithm**. This project demonstrates core software engineering principles, including GUI development, algorithm implementation, multi-threading, and secure input validation.

## 🚀 Situation-Task-Action-Result (STAR Method)

*   **Situation:** There was a need for an intuitive, educational tool to demonstrate and experiment with foundational cryptographic techniques, moving beyond command-line interfaces.
*   **Task:** To design, develop, and deploy a robust desktop application that provides a seamless user experience for encrypting and decrypting messages using the Caesar Cipher.
*   **Action:** 
    *   **Engineered** the core Caesar Cipher algorithm from scratch in Python to handle character substitution based on a user-defined cryptographic key.
    *   **Designed and developed** a modern, responsive graphical user interface (GUI) using the Tkinter framework, featuring a custom preloader animation fetched dynamically via HTTP requests.
    *   **Implemented multi-threading** to prevent the UI from freezing during encryption/decryption operations, ensuring a smooth and professional user experience.
    *   **Integrated robust input validation** and error handling to secure the application against invalid inputs and ensure system stability.
*   **Result:** Successfully delivered a fully functional, production-ready desktop application that serves as an effective educational platform for students and developers to learn about classical cryptography, GUI programming, and software development best practices.

## 🔐 How the Caesar Cipher Algorithm Works

The Caesar Cipher is a **substitution cipher** where each letter in the plaintext is shifted a fixed number of positions down or up the alphabet.

1.  **Encryption:** For a given key `k`, each letter in the plaintext is shifted `k` positions forward in the alphabet.
    *   Example: With a key of 3, 'A' becomes 'D', 'B' becomes 'E', ..., 'Z' becomes 'C'.
2.  **Decryption:** The reverse process. Each letter in the ciphertext is shifted `k` positions backward in the alphabet to retrieve the original plaintext.

This application implements this algorithm, handling both uppercase and lowercase letters while ignoring non-alphabetic characters to preserve formatting.


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**⭐ If you found this project helpful, please give it a star on GitHub!**
