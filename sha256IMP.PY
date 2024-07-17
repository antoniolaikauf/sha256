def input_bit(text):

    unicodeText=[ord(x) for x in text] # text in unicode

    bytes=[bin(x)[2:].zfill(8) for x in unicodeText] # unicode in bytes

    bits=[]
    for byte in bytes:
        for bit in byte:
            bits.append(int(bit)) # tutte le stringhe bytes unite in una 

    return bits

# print(input_bit('ci'))

def bits_to_hex(bits):
    bitsF=[]
    start=4
    for x in range(0,len(bits) - 3, 4):
        bitsF.append(bits[x:start]) #dividere bits in 4 per hex
        start+=4
    hex=[]
    for x in bitsF:
        for i,y in enumerate(x):
            x[i] = str(y)
        a = "".join(x)
        hex.append(int(a,2))
    return  hex

print(bits_to_hex(input_bit('ci')))