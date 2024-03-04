import caesar

text = 'the quick brown fox jumps over the lazy dog'
key = 7
caesar.additional = ','

encodedText = caesar.encode(text, key, True)
decodedText = caesar.decode(encodedText, key, True)

print(f'Encoded: {encodedText}')
print(f'Decoded: {decodedText}')