import hashlib
import time

common_passwords = ["123456", "password", "qwerty", "letmein", "password123"]

target_password = "password"
target_hash = hashlib.sha256(target_password.encode()).hexdigest()

start = time.time()
for pw in common_passwords:
    guess_hash = hashlib.sha256(pw.encode()).hexdigest()
    if guess_hash == target_hash:
        print("Cracked password:", pw)
        break
end = time.time()

print("Time taken:", round(end - start, 6), "seconds")
