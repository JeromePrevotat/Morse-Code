import time
import playsound

morse_code = {
'.-'    : 'a', '-...'  : 'b', '-.-.'  : 'c', '-..'   : 'd', '.'     : 'e',
'..-.'  : 'f', '--.'   : 'g', '....'  : 'h', '..'    : 'i', '.---'  : 'j',
'-.-'   : 'k', '.-..'  : 'l', '--'    : 'm', '-.'    : 'n', '---'   : 'o',
'.--.'  : 'p', '--.-'  : 'q', '.-.'   : 'r', '...'   : 's', '-'     : 't',
'..-'   : 'u', '...-'  : 'v', '.--'   : 'w', '-..-'  : 'x', '-.--'  : 'y',
'--..'  : 'z',
' '     : ' ', '/'     : '\n',
'.----' : '1', '..---' : '2', '...--' : '3', '....-' : '4', '.....' : '5',
'-....' : '6', '--...' : '7', '---..' : '8', '----.' : '9', '-----' : '0'
}

MSG = '... --- ...'

#DECODING
def decode_message(morse_code, msg):
    #Get Number of Words in the Message
    nb_word = get_nb_words(msg)
    #Split the Message in Words
    words = split_words(msg, nb_word)
    #Remove Useless Spaces
    remove_spaces(words)
    #Split Letters
    msg_decoded = decode_msg(morse_code, words)
    print(msg_decoded)

def remove_spaces(words):
    i = 0
    while i < len(words):
        #End Space
        if words[i][len(words[i]) - 1] == ' ':
            words[i] = words[i][0:len(words[i]) - 1]
        if words[i][0] == ' ':
            words[i] = words[i][1:]
        i += 1

def get_nb_words(msg):
    nb_word = 1
    for c in msg:
        if c == '/':
            nb_word += 1
    return nb_word

def split_words(msg, nb_word):
    words = [''] * nb_word
    decoded_words = [''] * nb_word
    i = 0
    while nb_word != 0:
        words[i] = msg.split('/')[i]
        nb_word -= 1
        i += 1
    return words

def decode_msg(morse_code, words):
    i = 0
    msg_decoded = ''
    while i < len(words):
        j = 0
        last_space = 0
        decoded = ''
        while j < len(words[i]):
            if words[i][j] == ' ':
                decoded += decode_letter(morse_code, words[i][last_space:j])
                last_space = j + 1
            j += 1
        if j == len(words[i]):
            decoded += decode_letter(morse_code, words[i][last_space:j])
            msg_decoded += (decoded + ' ')
        i += 1
    return msg_decoded

def decode_letter(morse_code, letter):
    for key, value in morse_code.items():
        if key == letter:
            return value
    return letter


#ENCODING
def encode_letter(morse_code, letter):
    for key, value in morse_code.items():
        if letter == value:
            return key + ' '
    return letter

def encode_word(morse_code, word):
    encoded = [''] * len(word)
    i = 0
    while (i < len(word)):
        encoded[i] = encode_letter(morse_code, word[i])
        i += 1
    return encoded + ['/ ']

def encode_message(morse_code, msg):
    encoded = ''
    words = msg.split(' ')
    for w in words:
        s = ''.join(encode_word(morse_code, w))
        encoded += s
    return encoded


#PLAYING
def play_message(msg):
    # . = 1
    # - = 3
    # Space between Signals = 1
    # Space between Letter = 3
    # Space between Words = 7
    for c in msg:
        if c == '.':
            playsound.playsound('beep.wav')
            time.sleep(0.1)
        elif c == '-':
            playsound.playsound('beep.wav')
            time.sleep(0.3)
        elif c == ' ':
            time.sleep(0.3)
        elif c == '/':
            time.sleep(0.7)
    time.sleep(1)


#MAIN
if __name__ == '__main__':
    #Decode a Message
    decode_message(morse_code, MSG)
    #Encode a Message
    encoded = encode_message(morse_code, 'sos')
    print(encoded)
    #Play the encoded message
    play_message(encoded)
