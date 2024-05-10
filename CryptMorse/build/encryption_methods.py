'''
def text_to_morse(text):
    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

    morse_code = ' '.join(morse_code_dict[i.upper()] for i in text if i.upper() in morse_code_dict.keys())
    return morse_code
'''

def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--', '#': '#', ';': '-.-.-.', ':': '---...', 
        '-': '-....-', '_': '..--.-', ' ': '---', '@': '.--.-.', 'SOS': '...---...', '&': '&', '$': '$',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}', '<': '<', '>': '>', '|': '|', '\\': '\\', '`': '`', '^': '^', '~': '~', '/': '-..-.','=':'-...-', '+': '.-...-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-', '+': '.-.-.', '@': '.--.-.', '$': '...-..-',
        'a': '*.-', 'b': '*-...', 'c': '*-.-.', 'd': '*-..', 'e': '*.','f': '*..-.', 'g': '*--.', 'h': '*....', 
        'i': '*..', 'j': '*.-.--', 'k': '*-.-', 'l': '*.-..', 'm': '*--', 'n': '*-.', 'o': '*---', 'p': '*.--.', 
        'q': '*--.-', 'r': '*.-.', 's': '*...', 't': '*-', 'u': '*..-', 'v': '*...-', 'w': '*.--', 'x': '*-..-', 
        'y': '*-.--', 'z': '*--..'
    }
    morse_code = ''
    for char in text:
        morse_code += morse_code_dict.get(char, '') + ' '

    return morse_code.strip()

#print(text_to_morse("Hello World"))


def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():  # Only encrypt alphabets
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text


#print(vigenere_encrypt("Hello World", "KEY"))

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Only encrypt alphabets
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

#print(caesar_encrypt("Hello World", 3))

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

import random
import string

def aes_encrypt(plaintext, key):
    key = key.encode('utf-8')
    plaintext_bytes = plaintext.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext_bytes, AES.block_size)
    encrypted_data = cipher.encrypt(padded_plaintext)
    encrypted_text = base64.b64encode(encrypted_data)
    return encrypted_text.decode('utf-8')
    

#key = input("please enter 32 letter key: ")
#key = key.encode('utf-8')#get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
#print(aes_encrypt("Hello World", key))

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

def des_encrypt(text, key):
    # Pad the text with random letters to make it 16 characters long
    #text = text.ljust(16, random.choice(string.ascii_letters))

    # Convert the key to bytes
    key = key.encode('utf-8')
    plaintext_bytes = text.encode('utf-8')
    # Create a new DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)

    # Pad the text to be a multiple of 8 bytes
    padded_text = pad(plaintext_bytes, DES.block_size)

    # Encrypt the padded text using the DES cipher
    encrypted_text = cipher.encrypt(padded_text)

    # Encode the encrypted text to base64
    encrypted_text = base64.b64encode(encrypted_text)

    return encrypted_text.decode('utf-8')
#key = input("please enter 16 letter key: ")
#key = key.encode('utf-8') # DES key must be 8 bytes long
#print(des_encrypt("Hello World", key))

import winsound
import time
def play_morse_code(encrypted_text_morse):
    beep_duration = 100  # Duration of each beep in milliseconds
    beep_frequency = 1000  # Frequency of the beep in hertz

    # Play the Morse code as beeps
    for char in encrypted_text_morse:
        if char == '.':
            winsound.Beep(beep_frequency, beep_duration)
        elif char == '-':
            winsound.Beep(beep_frequency, beep_duration * 3)  # Longer beep for dash
        elif char == ' ':
            # Pause between words
            time.sleep(beep_duration * 7 / 1000)  # 7 units of beep duration for word spacing
            #winsound.sleep(beep_duration * 7)  # 7 units of beep duration for word spacing



