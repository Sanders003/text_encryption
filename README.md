# Text Encryption Application

Welcome to the Text Encryption Application! This application uses the Caesar Cipher technique for encrypting and decrypting text. It is implemented in Python and provides a simple command-line interface for users to encrypt or decrypt their messages.

## Table of Contents

- [Caesar Cipher Technique](#caesar-cipher-technique)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
  - [Encrypting a Message](#encrypting-a-message)
  - [Decrypting a Message](#decrypting-a-message)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Caesar Cipher Technique

The Caesar Cipher is a basic encryption method used to secure messages. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3:

- A becomes D
- B becomes E
- C becomes F

To decrypt the message, you shift the letters in the opposite direction by the same number. This technique is named after Julius Caesar, who used it to protect his private communications.

The Caesar Cipher is simple and easy to implement but is not very secure by modern standards as it is easily crackable. It serves as a good introductory example of classical cryptography.


## Features

- Encrypt text using the Caesar Cipher technique.
- Decrypt text that was encrypted using the Caesar Cipher technique.
- Simple and easy-to-use command-line interface.
- Configurable shift value for the Caesar Cipher.

## Installation

To use this application, you'll need to have Python installed on your machine. Follow these steps to set up the application:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sanders003/text_encryption.git
    cd text_encryption
    ```

2. **Install dependencies:**
    There are no external dependencies for this application. It uses Python's standard library.

## Usage

You can use the application through the command line. Simply run the Python script and follow the prompts:

```bash
python cipher.py
```

## Options

- To encrypt a text, enter `e`.
- To decrypt a text, enter `d`.
- To exit the application, enter any other key.

## Examples

### Encrypting a Message

1. Run the application:
    ```bash
    python cipher.py
    ```
2. Enter `e` to encrypt a text.
3. Input the text to be encrypted:
    ```
    Enter the text for Encrypting: hello world
    ```
4. Input the shift value:
    ```
    Enter the value of shift: 4
    ```
5. Output:
    ```
    After Encryption the text is lipps asvph
    ```

### Decrypting a Message

1. Run the application:
    ```bash
    python cipher.py
    ```
2. Enter `d` to decrypt a text.
3. Input the text to be decrypted:
    ```
    Enter the text for Decrypting: lipps asvph
    ```
4. Input the shift value:
    ```
    Enter the value of shift: 4
    ```
5. Output:
    ```
    After Decryption the text is hello world
    ```

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, please open an issue or submit a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is an open source application.

## Contact

If you have any questions or suggestions, feel free to reach out to me at [22cs01004@iitbbs.com](mailto:22cs01004@iitbbs.com)
Or comment your suggestions in the code after the 50th line in the 'caesar_en.py' file.

---

Thank you for using the Text Encryption Application! We hope it meets your encryption and decryption needs effectively.
