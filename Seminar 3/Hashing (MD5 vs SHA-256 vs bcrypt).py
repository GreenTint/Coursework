import hashlib
import bcrypt

password = b"MySecurePassword!"

md5_hash = hashlib.md5(password).hexdigest()
sha256_hash = hashlib.sha256(password).hexdigest()

bcrypt_hash = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
bcrypt_check = bcrypt.checkpw(password, bcrypt_hash)

print("MD5:", md5_hash)
print("SHA256:", sha256_hash)
print("bcrypt:", bcrypt_hash)
print("bcrypt verified:", bcrypt_check)
