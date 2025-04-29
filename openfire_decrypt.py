#!/usr/bin/env python3

from Crypto.Cipher import Blowfish
from Crypto.Hash import SHA1
import binascii


def decrypt_openfire_pass(ciphertext_hex: str, key: str) -> str:
    # Convert the key to SHA-1:
    sha1_key = SHA1.new(key.encode()).digest()

    # Decode the hex-encoded ciphertext
    ciphertext = binascii.unhexlify(ciphertext_hex)

    # Get IV (first 8 bytes) and actual ciphertext
    iv = ciphertext[:8]
    encrypted_data = ciphertext[8:]

    # Decrypt using Blowfish CBC
    cipher = Blowfish.new(sha1_key, Blowfish.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_data)

    # Strip padding (Openfire uses PKCS5/PKCS7-like padding)
    pad_len = decrypted[-1]
    return decrypted[:-pad_len].decode("utf-8")


# Enter our found ciphertext & key
ciphertext = "[PutYourCipherTextHere]"
key = "[PutYourKeyHere]"

print(decrypt_openfire_pass(ciphertext, key))
