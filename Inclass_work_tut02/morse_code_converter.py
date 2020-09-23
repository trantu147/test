Morse_Code_Dict = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..',' ':' '}

# function to encrypt the string using Morse_Code_Dict
def encrypt(message):
    cipher = ''

    for letter in message:
        if(letter!=' '):
            # look up the dictionary to add the
            # matching morse code along with a space to
            # separate between character
            cipher += Morse_Code_Dict[letter] + ' '
        else:
            # add space to differentiate between a
            # character and a word
            cipher += ' '

    return cipher

# function to decrypt the code using Morse_Code_Dict
def decrypt(code):
    # add an extra space to the end to access the last Morse code
    code += ' '
    decipher = ''
    citext = ''
    for letter in code:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                # get the position of the Morse code in Morse_Code_Dict
                pos = list(Morse_Code_Dict.values()).index(citext)
                # adding character from the position above to the string
                decipher += list(Morse_Code_Dict.keys())[pos]
                citext = ''

    return decipher

def main():
    message = input("Please input plain text that you want to convert here: ")
    result = encrypt(message.upper())
    print(result)

    result1 = decrypt(result)
    print(result1)

main()