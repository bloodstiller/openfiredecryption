
# Openfire Blowfish Decryption Script

This Python script is designed to decrypt passwords encrypted by the [Openfire XMPP server](https://www.igniterealtime.org/projects/openfire/), which uses Blowfish in CBC mode and SHA-1 for key derivation.

> This script is also useful for CTFs and pentesting labs — it works perfectly on [Hack The Box](https://hackthebox.com) machines like **`solarlabs`** and **`jab`**.

---

## Features

- Decrypts Blowfish-encrypted Openfire credentials
- Uses SHA-1 hashed key for decryption
- Lightweight and easy to use for testing environments
- Helpful in real-world pentests or during CTF challenges

---

## Usage

1. Install dependencies:

```bash
pip install pycryptodome
```

2. Update the script with your ciphertext and key:

```python
ciphertext = "[PutYourCipherTextHere]"
key = "[PutYourKeyHere]"
```

3. Run the script:

```bash
python3 openfire_decrypt.py
```

---

## Example

```python
ciphertext = "d0c3baad314dce9cfcaf504f96f367e9"
key = "openfireadmin"

print(decrypt_openfire_pass(ciphertext, key))
```


## Notes

- Openfire uses a custom encryption scheme that combines:
  - **Blowfish CBC**
  - **SHA-1 key hashing**
  - **PKCS5/PKCS7-style padding**
- This script assumes the ciphertext is in **hex** format.
- You’ll need to extract the key and encrypted password from an Openfire configuration or database.

---

## Tested On

✅ [Hack The Box - solarlabs](https://app.hackthebox.com/machines/solarlabs)  
✅ [Hack The Box - jab](https://app.hackthebox.com/machines/jab)

