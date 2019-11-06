"""Detect an AES ECB cipher text from a list of hex-encoded cipher's"""
import binascii
import base64
from Cryptodome.Cipher import AES

"""Take the first 16 bits and compare them to the next 16-bits of text.  If there is a repeat, score it and then pop it out as the new key.
Continue this trend until you have run out of text to detect"""

def detectECB(cipherText):
    testBits = b''
    originalText = cipherText
    repeatCount = 0
    finalData = []
    while len(cipherText) > 16:
            testBits = cipherText[0:16]
            bitCount = cipherText[16:].count(testBits)
            if testBits not in finalData and bitCount > 0:
                repeatCount += 1
                finalData.append(testBits)
            elif bitCount > 0:
                repeatCount +=1
            cipherText = cipherText[16:]
    return {'ciphertext': originalText, 'count':repeatCount}
            
def main():
    with open('Challenge 8.txt') as fh:
        detectedData = []
        lineCount = 0
        for line in fh:
            line = bytes.fromhex(line.strip())
            detectedData.append(detectECB(line))
            lineCount +=1
        print(detectedData)
        print(sorted(detectedData, key = lambda x: x['count'], reverse = True)[0])
        print(lineCount)
                
                
if __name__ == '__main__':
    main()