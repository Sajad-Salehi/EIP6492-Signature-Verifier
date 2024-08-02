from eth_utils import to_bytes, to_hex
from web3 import Web3

def concat(datas):
    """
    Concatenates a list of bytes-like objects or hex strings into a single byte array.
    """
    concatenated_bytes = b''.join(
        Web3.to_bytes(hexstr=data) if isinstance(data, str) and data.startswith('0x') else data for data in datas
    )
    return concatenated_bytes

def format_as_uint8_array(byte_data):
    """
    Formats byte data into a Uint8Array-like output.
    """
    return [int(b) for b in byte_data]

