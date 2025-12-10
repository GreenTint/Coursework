import hashlib

def compute_hash(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

# Update this path to where YOU saved Procmon.exe
sample = r"C:\Path\To\Procmon.exe"

print("MD5:    ", compute_hash(sample, "md5"))
print("SHA1:   ", compute_hash(sample, "sha1"))
print("SHA256: ", compute_hash(sample, "sha256"))
