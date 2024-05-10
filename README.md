
Definition of the Problem:
Ensuring the security and secrecy of messages sent between people is crucial in today's digital environment. Nevertheless, a lot of people lack the skills or supports necessary to put into practice efficient encryption methods to protect their communications. Furthermore, there is a rising demand for accessible alternative communication techniques for people with varying abilities.
The goal of this project is to create a Python application that enables users to encrypt messages using both traditional and non-traditional encryption techniques in an effort to address these issues. The program will provide users the freedom to select the encryption method of their choice from a list of available possibilities. After encryption, the message will be played via the device's speaker and shown on the screen as Morse code, which is a well-known communication format. Additionally, users will be able to decode communications they receive by reading the Morse code representation.

Background and Existing Solutions:
Sensitive data has been protected for years using traditional encryption techniques like the Vigenère and Caesar ciphers. Nevertheless, these algorithms could not offer sufficient security in the current digital environment as they are vulnerable to modern cryptographic attacks. In existing cryptographic applications, non-classical algorithms like DES and Advanced Encryption Standard (AES) are frequently utilized since they provide higher security assurances.
Currently available message encryption solutions frequently only address cryptographic approaches, ignoring other forms of communication that might improve accessibility for people with disabilities. An effective substitute for sending encrypted communications vocally is Morse code, which uses a straightforward encoding technique of dots and dashes.

Description of Work:
The project will involve the following key components:
1. User Interface: We will develop a user-friendly interface, allowing users to input their message and select their desired encryption technique from a list of options.
2. Encryption Algorithms: Utilizing Python libraries such as cryptography, we will implement a variety of classical and non-classical encryption algorithms, including Caesar cipher, Vigenère cipher, AES, and DES. Each algorithm will have its own function for encrypting and decrypting messages.
3. Morse Code Conversion: After encryption, the encrypted message will be converted into Morse code using Python functions. We will implement a mapping between letters, numbers, and symbols to their respective Morse code representations.
4. Display and Playback: The encrypted message in Morse code will be displayed on the user interface. Additionally, we will use Python libraries such as pydub to play the Morse code audio through the device's speaker, providing both visual and auditory feedback to the user.
5. Decryption: Users will also have the option to decrypt received messages by either copying the Morse code or by visually decoding the Morse code representation.

 
Literature review

The clever dot-dash communication technique known as Morse code originated in the 1830s when Samuel Morse and Alfred Vail worked together to devise a way to send messages over great distances. At the time, this ground-breaking technique transformed long-distance communication and set the stage for the telegraph networks that would eventually link people on different continents. The simplicity of Morse code belied its great power, allowing information to be sent quickly using a sequence of short and long signals.
Beyond its use in telegraphy, Morse code was significant during important historical periods like World War II. Morse code proved to be a lifeline for military soldiers during this turbulent time, enabling the quick and secure transmission of vital information across oceans and battlefields. Because of its unique rhythm and effectiveness, it was very useful during times of war when accurate communication was crucial for intelligence gathering and strategic coordination.
Even though current communication technologies have essentially replaced Morse code in everyday use, its applicability still exists in a number of specialized applications. One such situation is emergency communication, in which amateur radio operators—also referred to as "ham radio" enthusiasts—remain in need of knowing Morse code. During catastrophes and emergencies, when traditional communication networks can be downed or unavailable, these committed people are indispensable. They can send messages quickly and reliably thanks to Morse code, which is an essential communication tool in emergency situations.
In addition, Morse code is still used in groups like the Scouts for both symbolic and functional objectives. As part of their training, scouts learn Morse code and discover its usefulness for long-distance silent communication and signaling. In addition to its useful uses, Morse code reflects tradition and heritage, linking Scouts to a rich history of cooperation, communication, and discovery.
Given the continued significance of Morse code, this information security effort becomes even more important. Participants interact with a cultural and historical item while also gaining practical expertise in encryption techniques by converting plaintext into Morse code ciphertext. The project provides an entry point for comprehending the development of communication technology, from the historical telegraph systems to the contemporary digital encryption techniques.
The project also emphasizes the enduring value of Morse code as a form of expression and communication. Morse code is a monument to human creativity and adaptability in a time of digital interfaces and quick messaging. Through efforts such as the one put forth, people actively participate in Morse code, helping to preserve and promote it so that this classic mode of communication can continue to enthrall and inspire generations to come.
 
Project description:
In Order to implement Morse Code into our Project and create a strong hard to break code we used different approaches for us to carry out the project of converting plaintext into Morse code ciphertext utilizing different encryption algorithms, such as the Vigenère cipher, DES (Data Encryption Standard), and AES (Advanced Encryption Standard). The following are the methods by which each encryption algorithm can be used to produce the intended encryption:
Types of Algorithms Used 

1.	AES (Advanced Encryption Standard):

Symmetric encryption algorithms like AES are frequently employed to protect sensitive data.
In order to use AES for the project, the plaintext must first be encrypted with AES in order to create a binary ciphertext. Next, utilizing a predetermined mapping between binary sequences and Morse code symbols, the binary ciphertext is converted into Morse code.
AES encryption usually requires the specification of a block size, and a key. Following the selected encoding strategy, the binary output of AES encryption is mapped to Morse code symbols to create the ciphertext's Morse code representation.
2.	DES (Data Encryption Standard):
An older symmetric encryption technique that uses 64-bit data blocks is called DES.
DES encryption is used to convert the plaintext into a binary ciphertext, much as AES encryption. Next, utilizing a predetermined mapping between binary sequences and Morse code symbols, the binary ciphertext is translated into Morse code.
A key must be specified for DES encryption in order to carry out the encryption and decryption processes. Following the selected encoding strategy, the binary output of DES encryption is mapped to Morse code symbols to create the ciphertext's Morse code representation.
3.	Vigenère Cipher:
The Vigenère cipher encrypts plaintext using a keyword and is a polyalphabetic substitution cipher. In order to use the Vigenère cipher for the project, the plaintext must first be encrypted using a designated keyword. A predetermined mapping between letters and Morse code symbols is then used to encode the alphabetic characters that make up the final ciphertext into Morse code. In order to create the ciphertext, the Vigenère cipher encryption method entails repeating the keyword until it matches the length of the plaintext and then performing modular addition between the plaintext and keyword. The Vigenère ciphertext's alphabetic characters are mapped to Morse code symbols in accordance with the selected encoding method to create the ciphertext's Morse code representation.
4.	Caeser Cipher
Select a Shift Value: Find the shift value, represented by the letter "k," which tells you how many alphabetic places each letter in the plaintext will be shifted to. A shift value of 3, for instance, indicates that each letter will be swapped out for the letter three spots ahead in the alphabet. Iterate through each character in the plaintext to encrypt it. Apply the Caesar cipher encryption by shifting the character by the selected shift value if it is a letter. Make sure that the letter case—uppercase or lowercase—is preserved throughout the encryption process. Characters that are not alphabetic, such numerals or punctuation, don't change.


 
Conversion into Morse code

To perform the project using AES, DES, Caeser or the Vigenère cipher, the plaintext must first be encrypted using the selected encryption technique, and the ciphertext must then be encoded into Morse code symbols. Various encryption algorithms provide varying degrees of security and intricacy, enabling customization according to project specifications and targeted encryption potency. Encode into Morse Code: Create a Morse code out of the resultant ciphertext. Make a mapping from each alphabet letter to the corresponding Morse code sequence. Similarly, for each non-alphabetic character in the ciphertext, construct a Morse code representation.
Produce Morse Code Ciphertext: Using the mapping determined in the previous step, replace each character in the ciphertext with its matching Morse code representation. To create the Morse code ciphertext, concatenate each character's Morse code representation.
The final result of the implementation is the Morse Code Ciphertext, which is the original plaintext that has been converted into Morse code and encrypted using the different types of encryption algorithms previously mentioned.


Conclusion:
To sum it up, the goal of this project is to give users a straightforward yet powerful tool for safely encrypting, decrypting, and communications. We provide a flexible solution that tackles security and accessibility issues by combining non-classical and classical encryption methods with Morse code communication. We want to enable people to secure their communications and promote diversity in digital communication channels with our initiative.

