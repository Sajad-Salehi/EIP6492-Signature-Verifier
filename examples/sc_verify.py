from erc6492_signature_verifier import SignatureVerifier


# Initialize the verifier with your Web3 provider URL
verifier = SignatureVerifier("YOUR_WEB3_PROVIDER_URL")

# Example data
signature = "0x3fd7d9db811f8022863fe95182bc83be526f252d329072ad7f847c5025e6716a482701e05b232354df7bcbba978f41a9369d1bc0aa40636c4d869cf87ff6975b1c"  # Replace with the actual signature
message = "sgdrsgdfgdfsdfesdfsf"
signer = "0x512e2330e7971f360e355F38939C1fF6D5063409"  # Replace with the actual signer's Ethereum address

# Verify the signature
is_valid = verifier.verify_signature(signature, message, signer)
print(f"Signature valid: {is_valid}")