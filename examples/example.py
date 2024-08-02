# examples/example_usage.py

from src.signature_verifier import SignatureVerifier

def main():
    # Initialize the Verifier
    verifier = SignatureVerifier("")

    # Sample data
    signature = "0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef12345678"
    message = "This is a sample message."
    signer = "0x1234567890abcdef1234567890abcdef12345678"

    # Verify the signature
    is_valid = verifier.verify_signature(signature, message, signer)

    # Print the result
    if is_valid:
        print("Signature is valid!")
    else:
        print("Signature is invalid!")

if __name__ == "__main__":
    main()