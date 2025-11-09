
# two small classic ciphers: ceasor and vigenure

import string

alphabet = string.ascii_uppercase

def ceasar_encrypt(plaintext, shift):
    plaintext = plaintext.upper()
    result = []
    for ch in plaintext:
        if ch in alphabet:
            idx = (alphabet.index(ch) + shift) % 26
            result.append(alphabet[idx])
        else:
            result.append(ch)
    return "".join(result)

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    result = []
    ki = 0
    for ch in plaintext:
        if ch in alphabet:
            shift = alphabet.index(key[ki % len(key)])
            idx = (alphabet.index(ch) + shift) % 26
            result.append(alphabet[idx])
            ki += 1
        else:
            result.append(ch)
    return "".join(result)

print("ceasar: ", ceasar_encrypt("mari kismat ma ha jo", 3))
print("Vigenere: ", vigenere_encrypt("tumhari kami", "Jalali"))