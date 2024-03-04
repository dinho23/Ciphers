import vigenere

text = 'The quick brown fox jumps over the lazy dog,'
key = 'secretkey'
vigenere.additional = ','

encodedText = vigenere.encode(text, key, True)
decodedText = vigenere.decode(encodedText, key, True)

print(f'Encoded: {encodedText}')
print(f'Decoded: {decodedText}')