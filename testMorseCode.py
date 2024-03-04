import morseCode

text = 'The quick brown fox jumps over the lazy dog'

encodedText = morseCode.encode(text)
morseCode.printString(encodedText)

decodedText = morseCode.decode(encodedText)
print(decodedText)

encodedString = '_ .... .   __._ .._ .. _._. _._   _... ._. ___ .__ _.   .._. ___ _.._   .___ .._ __ .__. ...   ___ ..._ . ._.   _ .... .   ._.. ._ __.. _.__   _.. ___ __.'
print(encodedString)
decodedText2 = morseCode.decode(encodedString)
print(decodedText2)