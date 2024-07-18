'''
For SHA-256, the initial hash value, H(0), shall consist of the following eight 32-bit words, in 
hex:
 H0 = 6a09e667 (a)
 H1 = bb67ae85 (b)
 H2 = 3c6ef372 (c)
 H3 = a54ff53a (d)
 H4 = 510e527f (e)
 H5 = 9b05688c (f)
 H6 = 1f83d9ab (g)
 H7 = 5be0cd19 (h)
Questi valori sono i primi 32 bits della parte decimale della radice quadrata e primi 8 numeri primi 

428a2f98 71374491 b5c0fbcf e9b5dba5 3956c25b 59f111f1 923f82a4 ab1c5ed5
d807aa98 12835b01 243185be 550c7dc3 72be5d74 80deb1fe 9bdc06a7 c19bf174
e49b69c1 efbe4786 0fc19dc6 240ca1cc 2de92c6f 4a7484aa 5cb0a9dc 76f988da
983e5152 a831c66d b00327c8 bf597fc7 c6e00bf3 d5a79147 06ca6351 14292967
27b70a85 2e1b2138 4d2c6dfc 53380d13 650a7354 766a0abb 81c2c92e 92722c85
a2bfe8a1 a81a664b c24b8b70 c76c51a3 d192e819 d6990624 f40e3585 106aa070
19a4c116 1e376c08 2748774c 34b0bcb5 391c0cb3 4ed8aa4a 5b9cca4f 682e6ff3
748f82ee 78a5636f 84c87814 8cc70208 90befffa a4506ceb bef9a3f7 c67178f2


k sarebbre delle costanti che si useranno per mischiare con il digest e sarebbero  primi 32 bits della parte decimale della radice cubica dei primi 64 numeri primi 
'''


# Ch(x, y,z) = (x ^ y) xor (x  ^ z)

# Maj(x, y,z) = (x  y)(x  z)(y  z)



h = ['0x6a09e667', '0xbb67ae85', '0x3c6ef372', '0xa54ff53a', '0x510e527f', '0x9b05688c', '0x1f83d9ab', '0x5be0cd19']

k = ['0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4','0xab1c5ed5', '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe','0x9bdc06a7', '0xc19bf174', '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f','0x4a7484aa', '0x5cb0a9dc', '0x76f988da', '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7','0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967', '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc','0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85', '0xa2bfe8a1', '0xa81a664b','0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070', '0x19a4c116','0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3','0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7','0xc67178f2']


class initializer():
    def __init__(self,value):
        self.value= value

    def hex_to_bits(self):
        binaries=[bin(int(x[2:],16))[2:] for x in (self.value)] #hex to bits

        bits=[]
        for bit in binaries:
            bits.append(int(bit))
        print(bits)
        # print(len(str(bits[0])))

        # # TODO sistemare questo controllo
        # words = []
        # for binary in binaries:
        #     word = []
        # for b in binary:
        #     word.append(int(b))
        #     words.append((word, 32, 'BE'))
        # return words
    
valueK=initializer(k)
valueH=initializer(h)
valueH.hex_to_bits()
valueK.hex_to_bits()


def cicle(valueH):
    a=valueH[0]
    b=valueH[1]
    c=valueH[2]
    d=valueH[3]
    e=valueH[4]
    f=valueH[5]
    g=valueH[6]
    h=valueH[7]

    for x in range(64):
        pass

# print(cicle(h))