import datetime as dt
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWSYZ"
alphabet = list(alphabet)
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}
reverse_morse_dict = {value:key for (key,value) in morse_dict.items()}
print(reverse_morse_dict)

#Space between letters in 3 dits,
#Space between words is 7 dits.
#period in morse code is ".-.-.-"
today = dt.date.today()
current_time = dt.datetime.now()


def to_morsecode(string):
    message = ""
    seperated_message = ""
    for letter in string:
        letter = letter.upper()
        if letter in morse_dict:
            letter = morse_dict[letter]
            seperated_message += f"{letter} "
            message += letter
    print(f"Your message in morse code is:{message}")
def from_morsecode(string):
    string = string.split()
    message = ""
    for char in string:
        if char in reverse_morse_dict:
            message += reverse_morse_dict[char]

    print(f"The morse code translates to this:{message.capitalize()}.")
program = True
print("Welcome to the Morse Code English Translator!")
while program:
    user_choice = input("Would you like to translate a message into morse code or from morse code? ")
    if 'to' in user_choice:
        user_message = input("Type a message you want to translate into Morse Code! ")
        to_morsecode(user_message)
    elif 'from' in user_choice:
        user_message = input("Type a morse code message you want to translate from Morse Code! ")
        from_morsecode(user_message)
    else:
        print("Invalid user input")
