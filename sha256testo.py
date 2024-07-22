def input_bit(text):

    unicodeText=[ord(x) for x in text] # text in unicode

    bytes=[bin(x)[2:].zfill(8) for x in unicodeText] # unicode in bytes

    bits=[]
    for byte in bytes:
        for bit in byte:
            bits.append(bit) # tutte le stringhe bytes unite in una 
    return bits

# print(input_bit('ci'))

def bits_to_hex(bits):
    bitsF=[]
    start=4
    for x in range(0,len(bits) - 3, 4):
        bitsF.append(bits[x:start]) #dividere bits in 4 per hex
        start+=4

    pair_F_bit=''
    for x in bitsF:
        for i,y in enumerate(x):
            x[i] = str(y) #trasformare bit 
        a = "".join(x)
        pair_F_bit += hex(int(a,2)) [2:] # convertire int in hex e prendere solo 6 invece di 0x6
    return  pair_F_bit

# print(bits_to_hex(input_bit('ci')))

def fillzeros(bits,length=8,eldian='LE'):
    l=len(bits)
    if eldian=='LE':
        while l < length:
            bits.append(str(0))
            l=len(bits)
    else: 
        while l < length: 
            bits.insert(0,str(0))
            l=len(bits)
        
    return bits


# print(fillzeros(input_bit('ci'),32))

'''
Suppose that the length of the message, M, is l bits. Append the bit “1” to the end of the 
message, followed by k zero bits, where k is the smallest, non-negative solution to the equation 
l + 1 + k=  448mod512
. Then append the 64-bit block that is equal to the number l expressed 
using a binary representation. For example, the (8-bit ASCII) message “abc” has length 
8 x 3 =  24, so the message is padded with a one bit, then 
448 - (24  + 1) = 423 zero bits, and then  the message length, to become the 512-bit padded message
'''

def padding(bits, lengthM):
    bits.append(str(1)) # ISO padding 

    while len(bits) % 512 !=448:
        bits.append(str(0))
    
    bits+=[x for x in bin(lengthM)[2:].zfill(64)] # aggunta rimanenti 64 bit che rappresentano lunghezza messaggio 

    return bits

message=input_bit('ciao')
# print(padding(message, len(message)))

def chunks(bits,chunk=8): #divide in chunk 512 bits a 32 bits
    chunks_bits=[]
    Lbits=len(bits)
    for x in range(0,Lbits,chunk):
        chunks_bits.append(bits[x:x + chunk])

    return chunks_bits 

# print(len(chunks(padding(message, len(message)),32)[0]))