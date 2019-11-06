import binascii
import base64
from codecs import EncodedFile

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

#Open the file, go through every line and apply the singleBitCipher function.
#Whichever line has the highest score out of all lines is most likely the one which has been encrypted 
#Print the unencrypted line and produce the cipher used

def detectSingleCipher(file1):
    cipherList = []
    for line in open(file1): #Opens the file and goes through it line by line adding all of the results in the format {'msg': bytes, 'Cipher': cipher used, 'score': final Score } in a list
        cipherList.append(singleBitCipher(bytes.fromhex(line[:60])))
    print(sorted(cipherList, key = lambda x: x['score'], reverse = True)[0]['msg']) #this line sorts the list of dictionary's by the score value in descending order and then prints out the first item in the list.
        
#singleBitCipher(binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
detectSingleCipher('Cipher.txt')

