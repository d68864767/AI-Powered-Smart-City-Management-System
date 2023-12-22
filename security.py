```python
# Import necessary libraries
import os
import json
import hashlib
import hmac
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Security
class Security:
    def __init__(self, secret_key):
        self.secret_key = secret_key.encode()

    def generate_encryption_key(self):
        # Generate a URL-safe 32-byte key. This must be kept secret.
        key = Fernet.generate_key()
        return key

    def encrypt_data(self, data, key):
        # Encrypt the data
        f = Fernet(key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data, key):
        # Decrypt the data
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data).decode()
        return decrypted_data

    def hash_data(self, data):
        # Hash the data
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        return hashed_data

    def hmac_data(self, data):
        # Create a new HMAC object
        h = hmac.new(self.secret_key, data.encode(), hashlib.sha256)
        return h.hexdigest()

    def generate_rsa_keys(self):
        # Generate a new RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def serialize_rsa_keys(self, private_key, public_key):
        # Serialize the keys
        pem_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        pem_public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem_private, pem_public

    def rsa_encrypt_data(self, data, public_key):
        # Encrypt the data with the public key
        encrypted_data = public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def rsa_decrypt_data(self, encrypted_data, private_key):
        # Decrypt the data with the private key
        decrypted_data = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_data.decode()

# Initialize security
security = Security('your_secret_key')

# Generate encryption key
key = security.generate_encryption_key()

# Encrypt data
encrypted_data = security.encrypt_data('your_data', key)

# Decrypt data
decrypted_data = security.decrypt_data(encrypted_data, key)

# Hash data
hashed_data = security.hash_data('your_data')

# HMAC data
hmac_data = security.hmac_data('your_data')

# Generate RSA keys
private_key, public_key = security.generate_rsa_keys()

# Serialize RSA keys
pem_private, pem_public = security.serialize_rsa_keys(private_key, public_key)

# RSA encrypt data
rsa_encrypted_data = security.rsa_encrypt_data('your_data', public_key)

# RSA decrypt data
rsa_decrypted_data = security.rsa_decrypt_data(rsa_encrypted_data, private_key)
```
