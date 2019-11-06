'''
Created on Feb 27, 2019

@author: Nick
'''
import binascii, base64
from itertools import count

def hamming2(x,y):
    """Calculate the Hamming distance between two bytes
    This code takes two bytes, asserts they are the same length and then XOR's each byte against each other.
    After each byte is XOR'ed, it converts the integer into it's binary code and counts how many '1''s appear.  This is the hamming distance between those two bytes.
    The code then adds this to the variable 'hammingDist' for output."""
    hammingDist = 0
    assert len(x) == len(y)
    for z in range(len(x)):
        hammingDist += bin(x[z]^y[z]).count('1') 
    return hammingDist


"""Takes the first KEYSIZE worth of bytes and finds the hamming distance between the two strings, then proceeds down the line 

    I want to try keysizes 2-40
    Take the length of the input, divide it by two.  len(input)/2 < 40, then max keysize = int((len(input)/2.floor()).  else max keysize = 40    
    for key in range(2, maxKeySize)
        results.append(normalizedDistance(inputBytes, key)
    sort the results by keysize and report the lowest hamming distance
    
"""
"""This function takes the normalized distance between an input of bytes and a certain keysize.  It iterates along the bytes until
it reaches the end of the bytes and returns a library item of distance versus keysize to be used in later functions
"""
def normalizedDistance(inputBytes, keySize):
    count = 0
    normDist = 0
    while len(inputBytes) >= (2*keySize):
        normDist += (hamming2(inputBytes[:keySize], inputBytes[keySize:keySize*2])/keySize)
        count += 1
        inputBytes = inputBytes[(keySize*2):]
    results = {'distance': (normDist/count), 'testKeySize': keySize}
    return results

def findKeySize(inputBytes):
    results = []
    if len(inputBytes)/2 < 40:
        maxKeySize = int((len(inputBytes)/2))
    else:
        maxKeySize = 40
    for key in range(2, maxKeySize+1):
        results.append(normalizedDistance(inputBytes, key))
    return sorted(results, key = lambda  x:x['distance'])[0]['testKeySize']

"""This function will take an input of bytes and break it into a list of chunks based on the key size such that every item in chunk 1 will be the"""
"""It is going to be a list with a for loop that will iterate along the length of the input.  
"""

def breakdown(inputBytes, keySize):
    chunks = [] #This is the list that will contain all of the byte arrays
    
    for x in range(0,keySize): #This for loop creates a bytearray for every one of the groups of letters encoded by a single character
        chunks.append(bytearray())
    
    for x in range(0, len(inputBytes), keySize): #Takes a keySize chunk of the text and puts each letter into it's corresponding bytearray in the chunks list
        try:
            count = 0
            while count < keySize:
                chunks[count].append(inputBytes[count+x])
                count +=1
        except:
            break
    return chunks

#Takes a series of bytes, converts the bytes into ASCII characters and then runs them against a score table utilizing ETAOIN SHRDLU as the scoring mechanism
def scoreCipher(byte1):
    scoreTable = {' ':24, 'e': 12.7, 't':9.0, 'a':8.2, 'o':7.5, 'i':7.0, 'n':6.7, 's':6.3, 'h':6.1, 'r':6.0, 'd':4.2, 'l':4.0, 'c':2.8, 'u':2.8, 'm':2.4, 'w':2.4, 'f':2.3, 'g':2.0, 'y':2.0,'p':1.9, 'b':1.5, 'v':1.0, 'k': 0.8, 'j': 0.15, 'x':0.15, 'q':0.1, 'z':0.1}
    currentScore = 0
    for x in byte1:
        if chr(x).lower() in scoreTable:
            currentScore += scoreTable[chr(x).lower()]
    return currentScore

#This formula takes bytes and an integer associated with an ascii text(possible cipher), XOR's each byte in the array by the cipher and returns the encoded byte array
def singleXor(byte1, cipher):
    encodeByte = b''
    for y in range(len(byte1)):
        encodeByte += bytes([(byte1[y] ^ cipher)])
    return encodeByte
        
#This function takes a string of encoded bytes, Xor's it against every possible ascii character from 0-127 and then scores it using the scoreCipher function.
#The 'msg', 'Cipher', and 'score' are then grouped together into a dictionary and put into a list of dictionaries.  This list is then sorted in descending order by using the sorted command with an anonymous function embedded in the key 

def singleBitCipher(encode):
    finalList = []
    for x in range(128):
            ansr = singleXor(encode, x)
            finalList.append({'msg': ansr, 'Cipher': x, 'score': scoreCipher(ansr)})
    return sorted(finalList, key = lambda x: x['score'], reverse = True)[0]

def main():
    key = ''
    with open('Challenge 8.txt') as input_file:
        decrypted = []
        finalText = b''
        finalKey = b''
        cipherText = b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j'
        keySize = findKeySize(cipherText)
        text = breakdown(cipherText, 16)
        for chunk in text:
            decrypted.append(singleBitCipher(chunk))
        """Now I need to iterate through the decrypted list of dictionaries and put together the string using """
        count = 0
        while count < len(decrypted[0]['msg']):
            for msg in decrypted:                
                try:
                    finalText += bytes([msg['msg'][count]])                    
                except:
                    break
            count += 1
        key = ''.join([chr(x['Cipher']) for x in decrypted])
        print(finalText)
        print(key)


if __name__ == '__main__':
    main()
