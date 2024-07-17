
def input_bit(text):

    unicodeText=[ord(x) for x in text] # text in unicode

    bytes=[bin(x)[2:].zfill(8) for x in unicodeText] # unicode in bytes

    bits=[]
    for byte in bytes:
        for bit in byte:
            bits.append(int(bit)) # tutte le stringhe bytes unite in una 

    return bits

print(input_bit('ci'))

def bits_to_hex(bits):
    value_to_hex=[]
    start=4
    for x in range(0,len(bits) - 3, 4):
        value_to_hex.append(bits[x:start])
        start+=4
    return value_to_hex

print(bits_to_hex(input_bit('ci')))