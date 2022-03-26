import numpy as np
def enc(text,enc_key):
    key = int(enc_key)
    #input
    text = str(text)
    ascii_values = []
    #text to ord()
    for character in text:
        ascii_values.append(ord(character))
    #python aray to numpy aray
    ac = np.array(ascii_values)
    #math enc
    ac = ac + key
    #from numpy aray back to python aray
    apa = list(ac)
    #back to text
    tapa = ''.join(chr(e) for e in apa)
    return tapa
def dec(enc_text,dec_key):
    key = int(dec_key)
    #input
    text = enc_text
    ascii_values = []
    #text to ord()
    for character in text:
        ascii_values.append(ord(character))
    #python aray to numpy aray
    ac = np.array(ascii_values)
    #math dnc
    ac = ac - key
    #from numpy aray back to python aray
    apa = list(ac)
    #back to text
    tapa = ''.join(chr(e) for e in apa)
    return tapa
def terminal_void(p):
    print(p)
