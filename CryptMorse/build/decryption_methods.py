'''
def morse_to_text(morse_code):
    text_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '}

    text = ''.join(text_dict[i] for i in morse_code.split(' ') if i in text_dict.keys())
    return text
'''

def morse_to_text(morse_code):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', 
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', 
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', 
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' ',
        '--..--': ',', '.-.-.-': '.', '..--..': '?', '-.-.--': '!', '#': '#', '-.-.-.': ';', '---...': ':', 
        '-....-': '-', '..--.-': '_', '---': ' ', '.--.-.': '@', '...---...': 'SOS', '&': '&', '$': '$',
        '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}', '<': '<', '>': '>', '|': '|', '\\': '\\', '`': '`', '^': '^', '~': '~', '-..-.': '/','-...-': '=','.-...-': '+','.-..-.': '"','-.--.': '(','-.--.-': ')','.-.-.': '+','.--.-.': '@','...-..-': '$',
        '*.-': 'a', '*-...': 'b', '*-.-.': 'c', '*-..': 'd', '*.': 'e', '*..-.': 'f', '*--.': 'g', '*....': 'h', 
        '*..': 'i', '*.-.--': 'j', '*-.-': 'k', '*.-..': 'l', '*--': 'm', '*-.': 'n', '*---': 'o', '*.--.': 'p', 
        '*--.-': 'q', '*.-.': 'r', '*...': 's', '*-': 't', '*..-': 'u', '*...-': 'v', '*.--': 'w', '*-..-': 'x', 
        '*-.--': 'y', '*--..': 'z'
    }
    decoded_text = ''
    morse_chars = morse_code.split(' ')
    for morse_char in morse_chars:
        decoded_text += morse_code_dict.get(morse_char, '')

    return decoded_text

#print(morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():  # Only decrypt alphabets
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

#print(vigenere_decrypt("Rijvs Gspvh", "KEY"))

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Only decrypt alphabets
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text

#print(caesar_decrypt("Khoor Zruog", 3))


from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import base64
from Crypto.Util.Padding import pad

def aes_decrypt(encrypted_data, key):
    key = key.encode('utf-8')
    encrypted_bytes = base64.b64decode(encrypted_data)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_bytes)
    return unpad(decrypted_data, AES.block_size).decode('utf-8')

#key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
#ciphered_text = b"U2FsdGVkX1+3ZW5kb2JqZWN0dG1sIHNlY3VyaXR5IGluIGJ5dGVz"
#print(aes_decrypt(ciphered_text, key))

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64

def des_decrypt(encrypted_text, key):
    key = key.encode('utf-8')
    encrypted_bytes = base64.b64decode(encrypted_text)
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_bytes)
    return unpad(decrypted_data, DES.block_size).decode('utf-8')
#key = get_random_bytes(8)  # DES key must be 8 bytes long
#ciphered_text = b"U2FsdGVkX1+3ZW5kb2JqZWN0dG1sIHNlY3VyaXR5IGluIGJ5dGVz"
#print(des_decrypt(ciphered_text, key))

import sounddevice as sd
import numpy as np
import time

import sounddevice as sd
import numpy as np

def listen_morse_code():
    # Set the sample rate and duration for recording
    sample_rate = 44100  # Adjust according to your microphone
    duration = 5  # Adjust the duration as needed

    # Start recording from the microphone
    print("Listening to Morse code...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Convert the recorded audio to Morse code
    morse_code = convert_audio_to_morse(recording, sample_rate)

    # Print the Morse code
    print("Morse code:", morse_code)

def convert_audio_to_morse(audio, sample_rate):
    # Convert the audio to mono and normalize the amplitude
    audio_mono = np.mean(audio, axis=1)
    audio_normalized = audio_mono / np.max(np.abs(audio_mono))

    # Apply a threshold to detect the presence of sound
    threshold = 0.9  # Adjust the threshold as needed
    audio_thresholded = np.where(audio_normalized > threshold, 1, 0)

    # Convert the audio to Morse code
    morse_code = ""
    dot_duration = 0.1  # Adjust the dot duration as needed
    dash_duration = 3 * dot_duration  # Adjust the dash duration as needed
    space_duration = 7 * dot_duration  # Adjust the space duration as needed

    is_sound = False
    sound_start_time = 0

    for i in range(len(audio_thresholded)):
        if audio_thresholded[i] == 1 and not is_sound:
            is_sound = True
            sound_start_time = i / sample_rate
        elif audio_thresholded[i] == 0 and is_sound:
            is_sound = False
            sound_duration = (i / sample_rate) - sound_start_time

            if sound_duration < dot_duration:
                morse_code += "."
            elif sound_duration < dash_duration:
                morse_code += "-"
            elif sound_duration < space_duration:
                morse_code += " "
    
    return morse_code

# Example usage
#listen_morse_code()



