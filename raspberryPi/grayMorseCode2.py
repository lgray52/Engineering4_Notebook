from time import sleep
import board
import digitalio

morseCode = { 'A':'.-', 'B':'-...',
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
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
    
interval = .25

led = digitalio.DigitalInOut(board.GP15)  # set up red led, connect to bottom right pin
led.direction = digitalio.Direction.OUTPUT

while True:
    print(f"Input text to translate to morse code, or press -q to quit")
    txt = input().split(' ')  # split the words
    
    if txt == ['-q']:
        break  # break the loop on the quit command
    
    else:
        translation = []
        for i in range(len(txt)):  # for each word
            upperCase = txt[i].upper()  # convert to upper case
            for letter in upperCase:
                translation.append(morseCode[letter]) # translate each letter
                translation.append(' ') # add space after each letter
            translation.append('/')  # add slash between each word
        
        fullMessage = ''.join(translation)  # join list into one string
        print(fullMessage)
        
        for character in fullMessage:
            # print(character)
            if character == '.':
                led.value = True
                sleep(interval)  # for dot, blink for interval
                led.value = False
            
            if character == '-':
                led.value = True
                sleep(interval*3)  # for dash, blink for three times as long as for a dot
                led.value = False

            if character == ' ':
                sleep(interval*3)  # between letters, pause for dash length
            
            if character == '/':
                sleep(interval*7)  # between words, pause for seven times as long as a dot
            
            sleep(interval)  # pause for a dot length between each character

            led.value = False  # make sure the led is turned off at the end
            
