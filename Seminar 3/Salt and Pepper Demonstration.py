import os
import hashlib

PEPPER = b"SECRET_PEPPER_VALUE"

def hash_no_salt(password: bytes):
    return hashlib.sha256(password).hexdigest()

def hash_with_salt(password: bytes, salt: bytes):
    return hashlib.sha256(password + salt).hexdigest()

def hash_with_salt_pepper(password: bytes, salt: bytes):
    return hashlib.sha256(password + salt + PEPPER).hexdigest()

pw = b"user123password"

salt1 = os.urandom(16)
salt2 = os.urandom(16)

print("No salt:", hash_no_salt(pw))
print("No salt again:", hash_no_salt(pw))
print("Salted 1:", hash_with_salt(pw, salt1))
print("Salted 2:", hash_with_salt(pw, salt2))
print("Salt + pepper:", hash_with_salt_pepper(pw, salt1))
