import string

# message = 'Python is Awesome'
message = 'Hello World'
shift = 3
alphabet = string.ascii_lowercase

FIRST_CHAR_CODE = 65
LAST_CHAR_CODE = 90
CHAR_RANGE = 26


def translate_message(message, shift):
    # pass

    result = ""

    # iterate through each letter in message
    for char in message.upper():
        if char.isalpha():
            # convert character to ascii code
            # returns integer representing unicode char
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
                # converts integer to unicode char
            new_char = chr(new_char_code)

            # loop through empty result string and append new char
            result += new_char
        else:
            result += char

        # print(char, char_code, new_char_code, new_char)
    print(result)


translate_message('Hello World', 3)
