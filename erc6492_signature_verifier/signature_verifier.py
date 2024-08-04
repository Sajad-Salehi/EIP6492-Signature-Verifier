from web3 import Web3
from .concat import concat
from .hash_msg import hash_message
from .binary_data import binary_data
from eth_abi import encode
from hexbytes import HexBytes
from eth_account.messages import encode_defunct

class SignatureVerifier:
    def __init__(self, web3_provider: str):
        self.w3 = Web3(Web3.HTTPProvider(web3_provider))
    
    def verify_signature(self, signature: str, message: str, signer: str) -> bool:

        signer_pb = Web3.to_checksum_address(signer)
        """Public method to verify a signature based on its length."""
        if len(signature) > 132:
            return self._verify_sc_signature(signature, message, signer_pb)
        else:
            return self._verify_eoa_signature(signature, message, signer_pb)
    
    def _verify_sc_signature(self, signature: str, message: str, signer: str) -> bool:
        """Internal method to verify a smart contract signature."""
        try:
            # Get the hash of the signed message
            hashed_message = hash_message(message)
    
            # Convert signature and message to bytes
            signature_bytes = Web3.to_bytes(hexstr=signature)
            message_bytes = Web3.to_bytes(hexstr=hashed_message)
    
            encoded_data = encode(
                ['address', 'bytes32', 'bytes'],
                [signer, message_bytes, signature_bytes]
            )
    
            # Perform the eth_call
            response = self.w3.eth.call({
                "data": concat([binary_data, encoded_data])
            })
    
            # Convert response to hex and check result
            hex_res = Web3.to_hex(response)
            return hex_res == '0x01'
    
        except Exception as e:
            self._log_error(f"An error occurred in _verify_sc_signature: {e}")
            return False
    
    def _verify_eoa_signature(self, signature: str, message: str, signer: str) -> bool:
        """Internal method to verify an externally owned account (EOA) signature."""
        try:
            encoded_msg = encode_defunct(text=message)
            signer_address = self.w3.eth.account.recover_message(
                encoded_msg,
                signature=HexBytes(signature)
            )
            return signer_address == signer
    
        except Exception as e:
            self._log_error(f"An error occurred in _verify_eoa_signature: {e}")
            return False
    
    def _log_error(self, message: str):
        """Internal method to log errors."""
        print(message) 
