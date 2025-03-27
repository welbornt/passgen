# passgen.py

This Python script generates a random password based on user-specified criteria.

## Features

- Generates passwords of a specified length.
- Allows users to specify the number of special characters, numbers, uppercase letters, and lowercase letters.
- Provides an option to save the generated password to a file.
- Includes basic input validation to prevent invalid password configurations.
- If a character count vlaue is set to 0 the password will not use that character type.

## Requirements

- Python 3

## Usage

1. **Clone or download passgen:**

    ```bash
    git clone <repository_url>
    ```

    or download the python file directly.

2. **Run passgen from the command line:**

    ```bash
    python3 passgen.py [options]
    ```

## Options

- `-L`, `--length`: Length of the password (default: 12).
- `-s`, `--special`: Number of special characters (punctuation) in the password (default: 2).
- `-n`, `--numbers`: Number of numbers in the password (default: 2).
- `-c`, `--capital`: Number of capital letters in the password (default: 2).
- `-l`, `--lower`: Number of lowercase letters in the password (default: 2).
- `-f`, `--file`: File path to save the password to.

## Examples

- Generate a password with default settings:

    ```bash
    python3 passgen.py
    ```

- Generate a password with length 16, 4 special characters, 4 numbers, 4 capital letters, and 4 lowercase letters:

    ```bash
    python3 passgen.py -L 16 -s 4 -n 4 -c 4 -l 4
    ```

- Generate a password and save it to a file named `password.txt`:

    ```bash
    python3 passgen.py -f password.txt
    ```

- Generate a password of length 20, and save it to a file named mysecurepassword.txt

    ```bash
    python3 passgen.py -L 20 -f mysecurepassword.txt
    ```

- Generate a password of length 100 using only special characters:

    ```bash
    python3 passgen.py -L 100 -n 0 -c 0 -l 0    
    ```

## Error Handling

- passgen will display an error message and exit if the specified password length is less than 8 or greater than 128.
- passgen will display an error message and exit if the sum of special, numbers, capital, and lowercase characters exceeds the specified password length.

## Script Description

passgen utilizes the `argparse` module to handle command line arguments, and the `random` and `string` modules to generate the password.

1. **Argument Parsing:**
    - passgen parses command-line arguments for password length, number of special characters, numbers, capital letters, lowercase letters, and file output.
2. **Input Validation:**
    - It checks if the password length is within the valid range (8-128).
    - It checks if the sum of character types does not exceed the password length.
3. **Password Generation:**
    - It initializes an empty list `password` to store the password characters.
    - It randomly places the specified number of special characters, numbers, capital letters, and lowercase letters in the password list.
    - It fills the remaining positions in the password list with random characters from the specified character sets.
4. **Output:**
    - It prints the generated password to the console or saves it to a file, as specified by the user.

## Note

- This script is a proof of concept only and should not be used in environments with high security requirements.
