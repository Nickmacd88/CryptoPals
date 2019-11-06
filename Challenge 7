import binascii
import base64
from Cryptodome.Cipher import AES

def main():
    with open('Challenge 7.txt') as fh:
        cipherText = base64.b64decode(fh.read())
        key = b'YELLOW SUBMARINE'
        cipher = AES.new(key, AES.MODE_ECB)
        plainText = cipher.decrypt(cipherText)
        print(plainText.decode())

if __name__ == '__main__':
    main()