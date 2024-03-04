import caesar
alphabet = 'abcdefghijklmnopqrstuvwxyz'
additional = ''

def transformKey(encryptionKey:str):
    permutations = alphabet + additional
    key = []
    for char in encryptionKey:
        key.append(permutations.find(char))
    return key

def encode(plainText: str, key: str, includeForeign = False):
    permutations = alphabet + additional
    caesar.additional = additional
    key = transformKey(key)
    indexKey = 0
    encryptedText = ''
    plainText = plainText.lower()

    for char in plainText:
        if char in permutations:
            encryptedText += caesar.encode(char, key[indexKey], includeForeign)
            indexKey += 1
            if indexKey >= len(key):
                indexKey = 0
        elif includeForeign:
            encryptedText += char

    return encryptedText

def decode(encodedText: str, key: str, includeForeign = False):
    permutations = alphabet + additional
    caesar.additional = additional
    key = transformKey(key)
    indexKey = 0
    decryptedText = ''
    encodedText = encodedText.lower()

    for char in encodedText:
        if char in permutations:
            decryptedText += caesar.decode(char, key[indexKey], includeForeign)
            indexKey += 1
            if indexKey >= len(key):
                indexKey = 0
        elif includeForeign:
            decryptedText += char

    return decryptedText
