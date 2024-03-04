alphabet = 'abcdefghijklmnopqrstuvwxyz'
additional = ''
includeForeign = True
encryptionKey = 3

def encode(plainText: str, key: int, includeForeign = False):
    permutations = alphabet + additional

    plainText = plainText.lower()

    encodedText = ''

    for char in plainText:
        if char in permutations:
            index = permutations.find(char) + key
            if index >= len(permutations):
                index = index % len(permutations)
            encodedText += permutations[index]
        elif includeForeign:
            encodedText += char
    return encodedText

def decode(encodedText: str, key: int, includeForeign = False):
    key = len(alphabet) + len(additional) - key
    return encode(encodedText, key, includeForeign)