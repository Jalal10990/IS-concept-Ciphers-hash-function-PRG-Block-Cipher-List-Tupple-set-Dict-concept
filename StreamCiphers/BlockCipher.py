# lab05_block.py
def feistel_round(L, R, k):
    # tiny round function: XOR R with k, then rotate and sum
    f = ((R ^ k) + ((R << 1) & 0xFF)) & 0xFF
    new_L = R
    new_R = L ^ f
    return new_L, new_R

def feistel_encrypt(block: bytes, keys):
    # block is 2 bytes (L, R) for simplicity
    L, R = block[0], block[1]
    for k in keys:
        L, R = feistel_round(L, R, k)
    return bytes([L, R])

def feistel_decrypt(block: bytes, keys):
    L, R = block[0], block[1]
    for k in reversed(keys):
        # inverse of the round (feistel structure is symmetric)
        R, L = feistel_round(R, L, k)
    return bytes([L, R])

# Demo
keys = [0x12, 0x34, 0x56, 0x78]  # round keys
plain = bytes([0x01, 0x02])
cipher = feistel_encrypt(plain, keys)
recovered = feistel_decrypt(cipher, keys)
print("Plain:", plain)
print("Cipher:", cipher)
print("Recovered:", recovered)
