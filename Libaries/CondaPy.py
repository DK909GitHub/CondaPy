def enc(text,enc_key):
    key = int(enc_key)
    #input
    text = str(text)
    ascii_values = []
    #text to ord()+key
    for character in text:
        ascii_values.append(ord(character)+key)
    #adds values in array as chr values
    tapa = ''.join(chr(e) for e in ascii_values)
    return tapa
def dec(text,dec_key):
    key = int(dec_key)
    #input
    text = str(text)
    ascii_values = []
    #text to ord()+key
    for character in text:
        ascii_values.append(ord(character)-key)
    #adds values in array as chr values
    tapa = ''.join(chr(e) for e in ascii_values)
    return tapa

