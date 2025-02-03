import time
import unicodedata

def normalize_string(string):
    normalized_string = unicodedata.normalize('NFKD', string.lower())
    return "".join([s for s in normalized_string if not unicodedata.combining(s)])

def write_message(string):
    alphabet = ' .,!?abcdefghijklmnopqrstuvwxyz'
    message = ''

    for string_letter in string:
        normalized_string = normalize_string(string_letter)

        for alphabet_letter in alphabet:
            print(f"{message}{alphabet_letter}", end='\r', flush=True)
            time.sleep(0.1)

            if alphabet_letter == normalized_string:
                message += string_letter
                break

    print(message)

user_input = input("Type some message (Do not use special characters): \r")
write_message(user_input)
