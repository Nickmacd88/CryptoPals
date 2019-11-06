import binascii

def fixedXOR(bit1, bit2):   #Takes two strings of bits and XOR's them against each other and returns a new bytes object
    ansr = bytes()
    for x in range(len(bit1)):
         ansr += (bit1[x] ^ bit2[x]).to_bytes(1, byteorder = 'little')
    return ansr

test = fixedXOR(binascii.unhexlify('1c0111001f010100061a024b53535009181c'),binascii.unhexlify('686974207468652062756c6c277320657965'))

print(binascii.hexlify(test).decode())
