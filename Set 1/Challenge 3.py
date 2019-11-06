import binascii

def scoreCipher(byte1):
    scoreTable = {' ':24, 'e': 12.7, 't':9.0, 'a':8.2, 'o':7.5, 'i':7.0, 'n':6.7, 's':6.3, 'h':6.1, 'r':6.0, 'd':4.2, 'l':4.0, 'c':2.8, 'u':2.8, 'm':2.4, 'w':2.4, 'f':2.3, 'g':2.0, 'y':2.0,'p':1.9, 'b':1.5, 'v':1.0, 'k': 0.8, 'j': 0.15, 'x':0.15, 'q':0.1, 'z':0.1}
    currentScore = 0
    for x in byte1:
        if chr(x) in scoreTable:
            currentScore += scoreTable[chr(x)]
    return currentScore

#Takes a string of bytes, XOR's it against every possible byte and scores each result.
def singleBitCipher(encode):
    finalByte = bytes()
    finalChar = 0
    finalScore = 0
    for x in range(128):
            ansr = bytes()
            for y in range(len(encode)):
                ansr += (encode[y] ^ x).to_bytes(1, byteorder = 'little')
            print (chr(x), ansr.decode(encoding = 'ascii'))
            #Now that the string has been encoded, we need to score it
            if finalScore < scoreCipher(ansr):
                finalScore = scoreCipher(ansr)
                finalChar = chr(x)
                finalByte = ansr
    print('The character was ', finalChar, ' and the phrase is', finalByte.decode())
                
            

singleBitCipher(binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
                