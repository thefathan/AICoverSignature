import hashlib

def hash_message(message: str) -> str:
    return hashlib.sha3_256(message.encode()).hexdigest()