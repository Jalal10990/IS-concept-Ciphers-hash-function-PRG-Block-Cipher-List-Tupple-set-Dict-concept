# lab06_hash.py
import hashlib

def sha256_hash(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()

# Demo with strings
text = "Hello, blockchain!"
digest = sha256_hash(text.encode())
print("SHA-256:", digest)

# Toy hash (educational only) - NOT secure
def toy_hash(data: bytes) -> int:
    # simple rolling: not collision resistant
    h = 0
    for b in data:
        h = ((h * 31) ^ b) & 0xFFFFFFFF
    return h

print("Toy hash (int):", toy_hash(text.encode()))
