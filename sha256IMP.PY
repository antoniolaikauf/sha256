def input_bit(text):
   
    unicodeText=[ord(x) for x in text]

    bytes=[bin(x)[2:].zfill(8) for x in unicodeText]

    bits=[]
    for byte in bytes:
        for bit in byte:
            bits.append(int(bit))

    return len(bits)


print(input_bit('ciao'))