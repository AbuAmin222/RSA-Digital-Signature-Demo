# RSA Digital Signature Demo

Chapter 02 (Cryptographic Tools) programming task for Software Security (SDEV 4303), Islamic University of Gaza.

The script generates a 2048-bit RSA key pair, signs a message with the private key (SHA-256, PKCS#1 v1.5), and verifies the signature with the public key. It then verifies a modified message with the same signature to show that tampering is detected.

## Requirements

- Python 3
- pycryptodome

## Run

```
pip install pycryptodome
python rsa_signature.py
```

## Expected output

```
Original message : VALID signature
Tampered message : INVALID signature
```

## How it works

1. A 2048-bit RSA key pair is generated.
2. The message is hashed with SHA-256.
3. The hash is signed with the private key.
4. The public key verifies the signature.
5. Changing even one word of the message changes the hash, so verification fails.