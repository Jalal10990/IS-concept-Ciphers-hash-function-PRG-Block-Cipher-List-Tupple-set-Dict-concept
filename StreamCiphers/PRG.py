# lab04_stream.py
def lcg(seed, a=1103515245, c=12345, m=2**31):
    """Simple LCG PRG yielding an infinite stream of bytes."""
    x = seed
    while True:
        x = (a * x + c) % m
        yield x & 0xFF  # yield lowest 8 bits

def xor_stream_encrypt(data: bytes, seed: int) -> bytes:
    key_stream = lcg(seed)
    out = bytearray()
    for b in data:
        k = next(key_stream)
        out.append(b ^ k)
    return bytes(out)

# Demo
message = b"Attack at dawn"
seed = 42
cipher = xor_stream_encrypt(message, seed)
plain = xor_stream_encrypt(cipher, seed)  # same operation decrypts
print("Cipher bytes:", cipher)
print("Decrypted:", plain)
