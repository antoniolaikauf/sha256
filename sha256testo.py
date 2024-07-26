def input_bit(text):

    unicodeText=[ord(x) for x in text] # text in unicode

    bytes=[bin(x)[2:].zfill(8) for x in unicodeText] # unicode in bytes

    bits=[]
    for byte in bytes:
        for bit in byte:
            bits.append(bit) # add all bits in a single list
    return bits

# print(input_bit('ci'))

def bits_to_hex(bits):
    bitsF=[]
    start=4
    for x in range(0,len(bits) - 3, 4):
        bitsF.append(bits[x:start]) #split 4 bits for hex
        start+=4
    # print(bitsF)
    pair_F_bit=''
    for x in bitsF:
        # for i,y in enumerate(x):
        #     x[i] = str(y) #trasformare bit 
        # a = "".join(x)
        pair_F_bit += hex(int(x,2)) [2:] # convert int in hex ed cut x0
    return  pair_F_bit

# print(bits_to_hex(input_bit('ci')))

def fillzeros(bits,length=8,eldian='LE'): # add 0 until lenght
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

# def padding(bits, lengthM):
#     bits.append(str(1)) # ISO padding 

#     while len(bits) % 512 !=448: # add 0 until reach 448 
#         bits.append(str(0))
    
#     bits+=[x for x in bin(lengthM)[2:].zfill(64)] # add remainig 64 bits to the list

#     return bits

# message=input_bit('ciao')
# print(padding(message, len(message)))


def padding(bits, lengthM):
    bits.append(str(1)) # ISO padding 
    array_bits=[]
    L=len(bits)
    if 448 < L < 512:
        bits+=[x for x in bin(lengthM)[2:].zfill(512 - L)]
    else:
        while len(bits) > 512:
            array_bits.append(bits[0:512])
            del bits[0:513]
        while len(bits) % 512 !=448: # add 0 until reach 448 
            bits.append(str(0))
        bits+=[x for x in bin(lengthM)[2:].zfill(64)] # add remainig 64 bits to the list

    array_bits.append(bits) 
    return array_bits

message=input_bit('ciattttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')
# print(padding(message, len(message)))

def chunks(bits,chunk=8): #split list of 512 bits in chucks of 32 bits
    chunks_bits=[]
    aMessage=[]
    for x in bits:aMessage +=x
    for x in range(0,len(aMessage),chunk):
        chunks_bits.append(aMessage[x:x + chunk])

    return chunks_bits

print(chunks(padding(message, len(message)),32))