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

    pair_F_bit=''
    for x in bitsF:
        for i,y in enumerate(x):
            x[i] = str(y) #trasformare bit 
        a = "".join(x)
        pair_F_bit += hex(int(a,2)) [2:] # convertire int in hex e prendere solo 6 invece di 0x6
    return  pair_F_bit

print(bits_to_hex(input_bit('ci')))


def fillZeros(bits, length=8, endian='LE'):
    #aggiungere 0 se messaggio è troppo breve di 512 bits
    while len(bits) < length :
        if endian == 'LE': bits.append(0) #aggiunto 0 a destra del messaggio  
        else:bits.insert(0,0) #aggiunto 0 a sinistra del messaggio 
    return bits 

print(fillZeros([1,0,1], 8, 'LE'))
print(fillZeros([1,0,1], 8, 'BE'))