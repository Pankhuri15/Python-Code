# Dictionary to encrypt message.
DICT = {'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '/': '-..-.',
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-',
        ' ': '/'}

# Dictionary to decrypt message.
DECRYPT_DICT = {value: key for (key, value) in DICT.items()}


def encrypt_message():
    message = [x for x in text]
    encrypt_list = [DICT[char] for char in message]
    string = ' '
    print(string.join(encrypt_list))


def decrypt_message():
    decrypt_list = [DECRYPT_DICT[code] for code in text_list]
    string = ''
    print(string.join(decrypt_list))


# Accepts input message.
text = input("Please enter the text: ").upper()
text_list = text.split()

# Sets default to decrypt.
option = "decrypt"

# Checks if the message has encrypted code. If not, sets the option to encrypt.
for element in text_list:
    if element not in DECRYPT_DICT:
        option = "encrypt"

if option == "encrypt":
    encrypt_message()
else:
    decrypt_message()



