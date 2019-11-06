import binascii

def repeatingKeyXor(msg, cipher):
    encryptedMsg = b''
    count = 0
    while count < len(msg):
        for x in cipher:
            try:
                encryptedMsg += bytes([msg[count] ^ x])
                count += 1
            except IndexError:
                break
    return encryptedMsg

print(binascii.hexlify(repeatingKeyXor("Several conventional names are used for collections or groups of bits.ByteHistorically, a byte was the number of bits used to encode a character of text in the computer, which depended on computer hardware architecture; but today it almost always means eight bits – that is, an octet. A byte can represent 256 (28) distinct values, such as non-negative integers from 0 to 255, or signed integers from −128 to 127. The IEEE 1541-2002 standard specifies (upper case) as the symbol for byte (IEC 80000-13 uses  for octet in French, but also allows  in English, which is what is actually being used). Bytes, or multiples thereof, are almost always used to specify the sizes of computer files and the capacity of storage units. Most modern computers and peripheral devices are designed to manipulate data in whole bytes or groups of bytes, rather than individual bits.".encode(), 'ICE'.encode())).decode())
        
            
#take a series of bytes and a cipher of x length, XOR the first byte by cipher[0] and add it too result, xor second byte by cipher[1] and add it too result,...last byte and cipher[x] and add it too the end.
#while int(len(decrypted bytes)/len(cipher).floor()) > 0 + len(decrypted bytes) mod len(cipher)
    #count = 0
    #encryptedText = b''
    # for x in cipher:
        #count += 1
        #encrypted += decrypted bytes[count] ^ x
        #
