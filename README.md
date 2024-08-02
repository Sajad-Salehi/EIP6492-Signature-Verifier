# EIP6492-Signature-Verifier

## Overview

The **erc6492_signature_verifier** library is a Python package designed to verify Ethereum signatures in compliance with EIP-6492. It supports both smart contract and externally owned account (EOA) signatures, automatically selecting the appropriate verification method based on the length of the signature. This library simplifies the process of signature verification for Ethereum-based applications.

## Features

- **Smart Contract Signature Verification**: Validates signatures associated with Ethereum smart contracts.
- **Externally Owned Account (EOA) Signature Verification**: Verifies signatures from externally owned accounts.
- **Automatic Method Selection**: Determines the appropriate verification method based on the signature length.

## Installation

You can install the **erc6492_signature_verifier** library from PyPI using pip:

```bash
pip install erc6492_signature_verifier
```

## Usage

Here’s a quick guide on how to use the `SignatureVerifier` class:

### Example

```python
from erc6492_signature_verifier import SignatureVerifier

# Initialize the verifier with your Web3 provider URL
verifier = SignatureVerifier("YOUR_WEB3_PROVIDER_URL")

# Example data
signature = "0x..."  # Replace with the actual signature
message = "Hello, world!"
signer = "0x..."  # Replace with the actual signer's Ethereum address

# Verify the signature
is_valid = verifier.verify_signature(signature, message, signer)
print(f"Signature valid: {is_valid}")
```

### Method Descriptions

- **`SignatureVerifier(web3_provider: str)`**: Initializes the verifier with the specified Web3 provider URL.
- **`verify_signature(signature: str, message: str, signer: str) -> bool`**: Verifies the given signature. The method automatically selects whether to use smart contract or EOA verification based on the signature length.

## Development

To contribute to the development of this library, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sajad-salehi/EIP6492-Signature-Verifier.git
   cd EIP6492-Signature-Verifier
   ```

2. **Install Development Dependencies**

   ```bash
   poetry install
   ```

3. **Run Tests**

   Execute the following command to run the tests:

   ```bash
   poetry run pytest
   ```

4. **Build and Publish**

   To build the library, use:

   ```bash
   poetry build
   ```

   To upload the package to PyPI, use:

   ```bash
   poetry publish --build --username __token__ --password YOUR_PYPI_TOKEN
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For issues or feature requests, please open an issue on the [GitHub repository](https://github.com/Sajad-Salehi/EIP6492-Signature-Verifier/issues).

For direct contact, email: [SajadSolidity@gmail.com](mailto:SajadSolidity@gmail.com)