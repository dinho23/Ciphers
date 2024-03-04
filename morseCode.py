morseCode = {'a':'._', 'b':'_...', 'c':'_._.', 'd':'_..', 'e':'.', 'f':'.._.', 'g':'__.', 'h':'....', 'i':'..',
             'j':'.___', 'k':'_._', 'l':'._..', 'm':'__', 'n':'_.', 'o':'___', 'p':'.__.', 'q':'__._', 'r':'._.',
             's':'...', 't':'_', 'u':'.._', 'v': '..._', 'w':'.__', 'x':'_.._', 'y':'_.__', 'z':'__..',
             '0':'_____', '1':'.____', '2':'..___', '3':'...__', '4':'...._', '5':'.....', '6':'_....', '7':'__...', '8':'___..', '9':'____.'}

def encode(text: str):
    text = text.lower()
    encodedText = []
    for char in text:
        if morseCode.get(char):
            encodedText.append(morseCode[char])
        else:
            encodedText.append(char)
    return encodedText

def decode(encodedText: list):
    if type(encodedText) == str:
        encodedText = stringToList(encodedText)
    
    decodedText = ''

    for item in encodedText:
        found = 0
        for key, value in morseCode.items():
            if value == item:
                decodedText += key
                found = 1
        if not found:
            decodedText += item

    return decodedText

def stringToList(string: str):
    formatedString = []
    letter = ''

    for i in range(0, len(string) - 1):
        if string[i] != ' ':
            letter += string[i]
        else:
            formatedString.append(letter)
            letter = ''
            if (string[i+1] == ' '):
                formatedString.append(' ')

    if letter != '':
        letter += string[-1]
        formatedString.append(letter)
    else:
        formatedString.append(string[-1])

    compressedString = []
    for item in formatedString:
        if item.strip() == '' and previous_item == ' ':
            continue
        compressedString.append(item)
        previous_item = item

    return compressedString


def printString(encodedText: list):
    for item in encodedText:
        print(item, end=' ')
    print('')

