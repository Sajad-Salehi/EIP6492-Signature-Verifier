import binascii
from typing import Union
import sha3


def hash_message(message: Union[bytes, str]) -> str:
    MessagePrefix = "\x19Ethereum Signed Message:\n"
    
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    prefix = f"{MessagePrefix}{len(message)}".encode('utf-8')
    prefixed_message = prefix + message
    
    # Use pysha3 to compute Keccak-256
    k = sha3.keccak_256()
    k.update(prefixed_message)
    digest = k.digest()
    hex_digest = binascii.hexlify(digest).decode('utf-8')
    
    return f"0x{hex_digest}"
