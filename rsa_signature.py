# pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
public_key = key.publickey()

def verify(msg, sig):
    try:
        pkcs1_15.new(public_key).verify(SHA256.new(msg), sig)
        return "VALID signature"
    except (ValueError, TypeError):
        return "INVALID signature"

msg = b"Transfer $1000 to Mark"
sig = pkcs1_15.new(key).sign(SHA256.new(msg))

print("Original message :", verify(msg, sig))
print("Tampered message :", verify(b"Transfer $1000 to Oscar", sig))