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
        
        print(' '.join(translation))  # join list into one string
